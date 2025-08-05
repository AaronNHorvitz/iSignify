from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List

from src.services.analysis_service import AnalysisService
from src.models.schemas import AnalysisResult

# Create a new router for our analysis endpoints
router = APIRouter()

@router.post("/analyze/", response_model=AnalysisResult, tags=["Analysis"])
async def run_analysis_endpoint(
    kmer_size: int = Form(..., description="The k-mer size for the analysis."),
    target_genome: UploadFile = File(..., description="The target genome file in FASTA format."),
    background_genomes: List[UploadFile] = File(..., description="One or more background genome files.")
):
    """
    Receives genome files and analysis parameters, then returns unique DNA signatures.
    """
    service = AnalysisService()
    try:
        # The service expects file-like objects, which UploadFile provides via .file
        result = service.run_analysis(
            target_file=target_genome.file,
            background_files=[bg_file.file for bg_file in background_genomes],
            kmer_size=kmer_size
        )
        return result
    except Exception as e:
        # If any error occurs during the analysis, return a 500 server error.
        raise HTTPException(status_code=500, detail=f"An error occurred during analysis: {str(e)}")