import pytest
from src.core.signature_finder import SignatureFinder

# --- Tests for the _generate_kmers helper method ---

def test_generate_kmers_correctly():
    """Tests that k-mers are generated correctly from a simple sequence."""
    # Arrange
    finder = SignatureFinder(kmer_size=4)
    sequence = "AGCTAGCT"
    expected_kmers = {"AGCT", "GCTA", "CTAG", "TAGC"}

    # Act
    result = finder._generate_kmers(sequence)

    # Assert
    assert result == expected_kmers

def test_generate_kmers_on_short_sequence():
    """Tests that an empty set is returned if the sequence is shorter than k."""
    # Arrange
    finder = SignatureFinder(kmer_size=10)
    sequence = "AGCT"

    # Act
    result = finder._generate_kmers(sequence)

    # Assert
    assert result == set()


# --- Tests for the main find_unique_signatures method (TDD) ---

def test_find_unique_signatures_simple_case():
    """
    Tests finding a single, simple unique signature region.
    This test will FAIL until the method is implemented.
    """
    # Arrange
    finder = SignatureFinder(kmer_size=3)
    target = {"t1": "AAATTTGGGCCC"}
    background = {"b1": "AAACCC"}
    # Expected unique region is "TTTGGG"
    expected_output = [{
        'sequence_id': 't1',
        'start': 3,
        'end': 9,
        'length': 6,
        'sequence': 'TTTGGG'
    }]

    # Act
    result = finder.find_unique_signatures(target, background)

    # Assert
    assert result == expected_output

def test_find_unique_signatures_merges_adjacent_kmers():
    """
    Tests that adjacent unique k-mers are correctly merged into one region.
    This test will FAIL until the method is implemented.
    """
    # Arrange
    finder = SignatureFinder(kmer_size=4)
    target = {"t1": "AAAGATTACACCC"} # Unique part is "GATTACA"
    background = {"b1": "AAACCC"}
    # The unique k-mers are GATT, ATTA, TTAC, TACA. They should merge.
    expected_output = [{
        'sequence_id': 't1',
        'start': 3,
        'end': 10,
        'length': 7,
        'sequence': 'GATTACA'
    }]

    # Act
    result = finder.find_unique_signatures(target, background)

    # Assert
    assert result == expected_output

def test_find_unique_signatures_none_found():
    """
    Tests that an empty list is returned when no unique signatures exist.
    This test will FAIL until the method is implemented.
    """
    # Arrange
    finder = SignatureFinder(kmer_size=5)
    target = {"t1": "GATTACA"}
    background = {"b1": "GATTACA"}

    # Act
    result = finder.find_unique_signatures(target, background)

    # Assert
    assert result == []