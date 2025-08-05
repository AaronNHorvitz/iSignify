from typing import List, IO
import tempfile
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.core.sequence_parser import SequenceParser
from src.core.signature_finder import SignatureFinder
from src.models.schemas import AnalysisResult, Signature

class AnalysisService:
    """
    This service class orchestrates the signature analysis process.
    It acts as a bridge between the API layer and the core logic.
    """

    def _generate_ai_summary(self, signature_count: int, kmer_size: int) -> str:
        """
        Generates a human-readable summary using the Gemma model.
        
        Note: For a production app, the model would be loaded once at startup,
        not on every API call. This is simplified for the hackathon.
        """
        try:
            # Use a smaller, faster version of Gemma for the hackathon
            model_name = "google/gemma-2b"
            
            # For CPU execution, specify the data type for better performance
            dtype = torch.bfloat16

            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=dtype,
            )

            # Create a clear prompt for the model
            prompt = f"You are a helpful bioinformatics assistant. Briefly summarize the following analysis result in a single, encouraging sentence. The analysis found {signature_count} unique DNA signatures using a k-mer size of {kmer_size}."

            input_ids = tokenizer(prompt, return_tensors="pt")

            # Generate the response
            response = model.generate(**input_ids, max_new_tokens=50)
            summary = tokenizer.decode(response[0], skip_special_tokens=True)
            
            # The model output includes the prompt, so we remove it.
            return summary[len(prompt):].strip()

        except Exception as e:
            # If the AI model fails, return a simple, default summary
            return f"Analysis complete. Found {signature_count} unique signature(s) using a k-mer size of {kmer_size}. AI summary failed: {str(e)}"


    def run_analysis(self, target_file: IO, background_files: List[IO], kmer_size: int) -> AnalysisResult:
        """
        Executes the full signature analysis pipeline.
        """
        parser = SequenceParser()
        finder = SignatureFinder(kmer_size=kmer_size)
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_target:
            tmp_target.write(target_file.read())
            tmp_target_path = tmp_target.name
        
        background_paths = []
        for bg_file in background_files:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_bg:
                tmp_bg.write(bg_file.read())
                background_paths.append(tmp_bg.name)

        try:
            target_sequences = parser.parse(tmp_target_path)
            background_sequences = {}
            for path in background_paths:
                background_sequences.update(parser.parse(path))

            found_signatures = finder.find_unique_signatures(
                target_sequences=target_sequences,
                background_sequences=background_sequences
            )

            # *** THIS IS THE NEW PART ***
            # Replace the placeholder with a real call to the Gemma model.
            summary = self._generate_ai_summary(len(found_signatures), kmer_size)

            result = AnalysisResult(
                summary=summary,
                signatures=[Signature(**sig) for sig in found_signatures]
            )
        finally:
            os.remove(tmp_target_path)
            for path in background_paths:
                os.remove(path)

        return result