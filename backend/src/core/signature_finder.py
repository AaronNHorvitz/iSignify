from typing import Dict, Set, List
class SignatureFinder:
    """
    Finds unique DNA sequences (signatures) in a target genome by comparing
    it against a set of background genomes.
    """

    def __init__(self, kmer_size: int):
        """
        Initializes the SignatureFinder.

        Args:
            kmer_size: The length of the k-mer to use for signature discovery.
                       A k-mer is a DNA sequence of a specific length 'k'.
        """
        self.kmer_size = kmer_size

    def _generate_kmers(self, sequence: str) -> Set[str]:
        """
        Generates a set of unique k-mers from a given DNA sequence.

        Args:
            sequence: The DNA sequence string.

        Returns:
            A set of unique k-mer strings found in the sequence.
        """
        if len(sequence) < self.kmer_size:
            return set() # Return an empty set if the sequence is too short

        return {
            sequence[i:i + self.kmer_size]
            for i in range(len(sequence) - self.kmer_size + 1)
        }

    def find_unique_signatures(
        self, target_sequences: Dict[str, str], background_sequences: Dict[str, str]
    ) -> List[Dict]:
        """
        The main analysis function to find and merge unique signature regions.
        """
        # Step 1: Build a single, efficient set of all background k-mers.
        background_kmers = set()
        for seq in background_sequences.values():
            background_kmers.update(self._generate_kmers(seq))

        all_signatures = []

        # Step 2: Process each target sequence individually.
        for seq_id, target_seq in target_sequences.items():
            
            # Step 3: Find the starting positions of all k-mers in the target
            # that are NOT present in the background set.
            unique_kmer_indices = [
                i
                for i in range(len(target_seq) - self.kmer_size + 1)
                if target_seq[i:i + self.kmer_size] not in background_kmers
            ]

            if not unique_kmer_indices:
                continue # No unique k-mers found in this sequence, move to the next.

            # Step 4: Merge consecutive k-mer indices into regions.
            merged_regions = []
            start_of_region = unique_kmer_indices[0]
            end_of_region_kmer_start = unique_kmer_indices[0]

            for i in range(1, len(unique_kmer_indices)):
                # Check if the current k-mer start is adjacent to the previous one
                if unique_kmer_indices[i] == end_of_region_kmer_start + 1:
                    end_of_region_kmer_start = unique_kmer_indices[i]
                else:
                    # The chain is broken, finalize the previous region
                    merged_regions.append((start_of_region, end_of_region_kmer_start))
                    # Start a new region
                    start_of_region = unique_kmer_indices[i]
                    end_of_region_kmer_start = unique_kmer_indices[i]
            
            # Add the last region after the loop finishes
            merged_regions.append((start_of_region, end_of_region_kmer_start))

            # Step 5: Format the merged regions into the final output structure.
            for start, end_kmer_start in merged_regions:
                # The end of the sequence is the end of the last k-mer in the chain
                end = end_kmer_start + self.kmer_size
                sequence_str = target_seq[start:end]
                
                all_signatures.append({
                    'sequence_id': seq_id,
                    'start': start,
                    'end': end,
                    'length': len(sequence_str),
                    'sequence': sequence_str
                })

        return all_signatures