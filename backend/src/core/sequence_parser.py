from typing import Dict

class SequenceParser:
    """A simple parser for reading FASTA formatted sequence files."""

    def parse(self, file_path: str) -> Dict[str, str]:
        """
        Reads a FASTA file and returns a dictionary of its sequences.

        This method handles multi-line sequences, correctly associating them
        with the preceding header.

        Args:
            file_path: The absolute or relative path to the FASTA file.

        Returns:
            A dictionary where keys are the sequence headers (e.g., '>seq1')
            and values are the corresponding DNA sequence strings.
        """
        sequences: Dict[str, str] = {}
        current_sequence_header = ""

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines

                    if line.startswith('>'):
                        current_sequence_header = line
                        sequences[current_sequence_header] = ""
                    elif current_sequence_header:
                        # Append the sequence data to the current header
                        sequences[current_sequence_header] += line
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return {}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

        return sequences