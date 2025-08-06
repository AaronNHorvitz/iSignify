import sys
import tempfile
from Bio import SeqIO

class FastaPreprocessor:
    """
    Processes FASTA files to ensure they are compatible with the iSignify pipeline.
    Specifically, it merges multi-contig files into a single-sequence format.
    """

    def process_file(self, input_path: str) -> str:
        """
        Checks a FASTA file, and if it's multi-contig, merges it.

        Args:
            input_path: The path to the input FASTA file.

        Returns:
            The path to the processed, single-sequence FASTA file.
            If no processing was needed, it returns the original input_path.
        """
        try:
            # Read all sequences from the input file 
            records = list(SeqIO.parse(input_path, "fasta"))

            # If there's more than one record, it's a multi-contig file 
            if len(records) > 1:
                print(f"Merging {len(records)} contigs from {input_path}")
                
                # Use the first record as the base for the merged sequence 
                merged_record = records[0]
                merged_sequence = str(records[0].seq)

                # Append subsequent records with a 100 'N' spacer 
                for record in records[1:]:
                    merged_sequence += 'N' * 100 + str(record.seq)
                
                merged_record.seq = merged_sequence
                
                # Create a new temporary file to store the result
                with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".fna") as tmp_file:
                    SeqIO.write(merged_record, tmp_file, "fasta")
                    return tmp_file.name
            else:
                # If only one sequence, no changes needed, return the original path 
                print("File already has one sequence; no changes needed.")
                return input_path
        except Exception as e:
            print(f"Error processing FASTA file {input_path}: {e}")
            # In case of error, return the original path to let the next step handle it
            return input_path