import pytest
from src.core.signature_finder import SignatureFinder

# --- Tests for the _generate_kmers helper method ---
# (These are unchanged and are passing)
def test_generate_kmers_correctly():
    finder = SignatureFinder(kmer_size=4)
    sequence = "AGCTAGCT"
    expected_kmers = {"AGCT", "GCTA", "CTAG", "TAGC"}
    result = finder._generate_kmers(sequence)
    assert result == expected_kmers

def test_generate_kmers_on_short_sequence():
    finder = SignatureFinder(kmer_size=10)
    sequence = "AGCT"
    result = finder._generate_kmers(sequence)
    assert result == set()


# --- Tests for the main find_unique_signatures method (with corrected expectations) ---

def test_find_unique_signatures_simple_case():
    # Arrange
    finder = SignatureFinder(kmer_size=3)
    target = {"t1": "AAATTTGGGCCC"}
    background = {"b1": "AAACCC"}
    
    # CORRECTED EXPECTED OUTPUT
    expected_output = [{
        'sequence_id': 't1',
        'start': 1,
        'end': 11,
        'length': 10,
        'sequence': 'AATTTGGGCC'
    }]

    # Act
    result = finder.find_unique_signatures(target, background)

    # Assert
    assert result == expected_output

def test_find_unique_signatures_merges_adjacent_kmers():
    # Arrange
    finder = SignatureFinder(kmer_size=4)
    target = {"t1": "AAAGATTACACCC"}
    background = {"b1": "AAACCC"}

    # CORRECTED EXPECTED OUTPUT
    expected_output = [{
        'sequence_id': 't1',
        'start': 0,
        'end': 12,
        'length': 12,
        'sequence': 'AAAGATTACACC'
    }]

    # Act
    result = finder.find_unique_signatures(target, background)

    # Assert
    assert result == expected_output

def test_find_unique_signatures_none_found():
    # (This test is unchanged and is passing)
    finder = SignatureFinder(kmer_size=5)
    target = {"t1": "GATTACA"}
    background = {"b1": "GATTACA"}
    result = finder.find_unique_signatures(target, background)
    assert result == []