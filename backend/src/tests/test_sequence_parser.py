import pytest
from src.core.sequence_parser import SequenceParser

@pytest.fixture
def fasta_file(tmp_path):
    """A pytest fixture to create a temporary FASTA file for testing."""
    # tmp_path is a built-in pytest fixture that provides a temporary directory
    fasta_content = """
>seq1 header for sequence one
GATTACA
GATTACA
>seq2 another sequence
AGCTAGCT
>seq3_third_sequence with no newline at end
ACGT
"""
    # Create a dummy file in the temporary directory
    p = tmp_path / "test.fna"
    p.write_text(fasta_content)
    return p


def test_parse_valid_fasta(fasta_file):
    """
    Tests that the parser correctly reads a valid, multi-line FASTA file.
    """
    # Arrange
    parser = SequenceParser()
    expected_output = {
        ">seq1 header for sequence one": "GATTACAGATTACA",
        ">seq2 another sequence": "AGCTAGCT",
        ">seq3_third_sequence with no newline at end": "ACGT",
    }

    # Act
    result = parser.parse(fasta_file)

    # Assert
    assert result == expected_output


def test_parse_nonexistent_file():
    """
    Tests that the parser returns an empty dictionary for a nonexistent file.
    """
    # Arrange
    parser = SequenceParser()

    # Act
    result = parser.parse("nonexistent/path/to/file.fna")

    # Assert
    assert result == {}