from typing import List, IO
import tempfile
import os

from src.core.sequence_parser import SequenceParser
from src.core.signature_finder import SignatureFinder
from src.models.schemas import AnalysisResult, Signature

class AnalysisService:
    """
    This service class orchestrates the signature analysis process.
    It acts as a bridge between the API layer and the core logic.
    """

    def run_analysis(self, target_file: IO, background_files: List[IO], kmer_size: int) -> AnalysisResult:
        """
        Executes the full signature analysis pipeline.

        Args:
            target_file: The file-like object for the target genome.
            background_files: A list of file-like objects for the background genomes.
            kmer_size: The k-mer size for the analysis.

        Returns:
            An AnalysisResult object containing the summary and signatures.
        """
        parser = SequenceParser()
        finder = SignatureFinder(kmer_size=kmer_size)
        
        # FastAPI's UploadFile is a file-like object. We need to save it to a
        # temporary file to get a path that our SequenceParser can read.
        with tempfile.NamedTemporaryFile(delete=False) as tmp_target:
            tmp_target.write(target_file.read())
            tmp_target_path = tmp_target.name
        
        background_paths = []
        for bg_file in background_files:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_bg:
                tmp_bg.write(bg_file.read())
                background_paths.append(tmp_bg.name)

        try:
            # Step 1: Parse all the sequence files
            target_sequences = parser.parse(tmp_target_path)
            
            background_sequences = {}
            for path in background_paths:
                background_sequences.update(parser.parse(path))

            # Step 2: Run the core signature finding logic
            found_signatures = finder.find_unique_signatures(
                target_sequences=target_sequences,
                background_sequences=background_sequences
            )

            # Step 3: (Placeholder for AI Integration) Generate a summary
            # We will replace this with a real call to the Gemma model in Phase 4.
            summary = f"Analysis complete. Found {len(found_signatures)} unique signature(s) using a k-mer size of {kmer_size}."

            # Step 4: Format the results using our Pydantic models
            result = AnalysisResult(
                summary=summary,
                signatures=[Signature(**sig) for sig in found_signatures]
            )
        finally:
            # Clean up the temporary files
            os.remove(tmp_target_path)
            for path in background_paths:
                os.remove(path)

        return result