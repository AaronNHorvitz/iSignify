import pytest
import os
from src.core.preprocessor import FastaPreprocessor

@pytest.fixture
def fasta_files(tmp_path):
    """A pytest fixture to create temporary single- and multi-contig FASTA files."""
    single_contig_content = ">seq1 single contig\nACGTACGT"
    multi_contig_content = ">contig1\nAAAA\n>contig2\nCCCC\n>contig3\nGGGG"
    
    single_path = tmp_path / "single.fna"
    single_path.write_text(single_contig_content)
    
    multi_path = tmp_path / "multi.fna"
    multi_path.write_text(multi_contig_content)
    
    return {"single": single_path, "multi": multi_path}


def test_preprocessor_on_single_contig_file(fasta_files):
    """
    Tests that the preprocessor does nothing to a file that is already
    in the correct single-sequence format.
    """
    # Arrange
    preprocessor = FastaPreprocessor()
    input_path = fasta_files["single"]

    # Act
    processed_path = preprocessor.process_file(input_path)

    # Assert
    # The path should be the same, as no new file should be created
    assert processed_path == input_path


def test_preprocessor_on_multi_contig_file(fasta_files):
    """
    Tests that the preprocessor correctly merges a multi-contig file
    into a new, single-sequence file.
    """
    # Arrange
    preprocessor = FastaPreprocessor()
    input_path = fasta_files["multi"]

    # Act
    processed_path = preprocessor.process_file(input_path)

    # Assert
    try:
        # The path should be different, as a new temp file was created
        assert processed_path != input_path
        
        # Verify the content of the new file
        with open(processed_path, 'r') as f:
            content = f.read()
            
            # Should only have one header
            assert content.count('>') == 1
            # Should contain the correct number of N-spacers
            assert content.count('N' * 100) == 2
            # Should contain the original sequences
            assert "AAAA" in content
            assert "CCCC" in content
            assert "GGGG" in content

    finally:
        # Clean up the temporary file created by the preprocessor
        if processed_path != input_path:
            os.remove(processed_path)