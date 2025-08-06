from typing import List, IO
import tempfile
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.core.sequence_parser import SequenceParser
from src.core.signature_finder import SignatureFinder
from src.core.preprocessor import FastaPreprocessor
from src.models.schemas import AnalysisResult, Signature

class AnalysisService:
    """
    This service class orchestrates the signature analysis process.
    It acts as a bridge between the API layer and the core logic.
    """

    def _generate_ai_summary(self, signature_count: int, kmer_size: int) -> str:
        """
        Generates a human-readable summary using the Gemma model.
        """
        try:
            model_name = "google/gemma-2b"
            dtype = torch.bfloat16
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=dtype)
            prompt = f"You are a helpful bioinformatics assistant. Briefly summarize the following analysis result in a single, encouraging sentence. The analysis found {signature_count} unique DNA signatures using a k-mer size of {kmer_size}."
            input_ids = tokenizer(prompt, return_tensors="pt")
            response = model.generate(**input_ids, max_new_tokens=50)
            summary = tokenizer.decode(response[0], skip_special_tokens=True)
            return summary[len(prompt):].strip()
        except Exception as e:
            return f"Analysis complete. Found {signature_count} unique signature(s) using a k-mer size of {kmer_size}. AI summary failed: {str(e)}"


    def run_analysis(self, target_file: IO, background_files: List[IO], kmer_size: int) -> AnalysisResult:
        """
        Executes the full signature analysis pipeline, including pre-processing.
        """
        parser = SequenceParser()
        finder = SignatureFinder(kmer_size=kmer_size)
        preprocessor = FastaPreprocessor()

        # Keep track of all temporary files that need to be cleaned up
        temp_files_to_clean = []

        try:
            # Save uploaded target file to a temporary path
            with tempfile.NamedTemporaryFile(delete=False, suffix=".fna") as tmp_target:
                tmp_target.write(target_file.read())
                temp_files_to_clean.append(tmp_target.name)
                
                # --- Run pre-processing on the target file ---
                processed_target_path = preprocessor.process_file(tmp_target.name)
                if processed_target_path != tmp_target.name:
                    temp_files_to_clean.append(processed_target_path)

            # Save uploaded background files to temporary paths
            background_paths = []
            for bg_file in background_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".fna") as tmp_bg:
                    tmp_bg.write(bg_file.read())
                    temp_files_to_clean.append(tmp_bg.name)
                    background_paths.append(tmp_bg.name)

            # --- Run pre-processing on all background files ---
            processed_background_paths = [preprocessor.process_file(p) for p in background_paths]
            for p in processed_background_paths:
                if p not in background_paths:
                    temp_files_to_clean.append(p)

            # Step 1: Parse all the PROCESSED sequence files
            target_sequences = parser.parse(processed_target_path)
            
            background_sequences = {}
            for path in processed_background_paths:
                background_sequences.update(parser.parse(path))

            # Step 2: Run the core signature finding logic
            found_signatures = finder.find_unique_signatures(
                target_sequences=target_sequences,
                background_sequences=background_sequences
            )

            # Step 3: Generate AI summary
            summary = self._generate_ai_summary(len(found_signatures), kmer_size)

            # Step 4: Format the results
            result = AnalysisResult(
                summary=summary,
                signatures=[Signature(**sig) for sig in found_signatures]
            )
        finally:
            # Clean up ALL temporary files
            for path in temp_files_to_clean:
                if os.path.exists(path):
                    os.remove(path)

        return result