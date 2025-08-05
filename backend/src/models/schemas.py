from pydantic import BaseModel
from typing import List

class Signature(BaseModel):
    """
    Represents a single unique DNA signature found by the analysis.
    """
    sequence_id: str
    start: int
    end: int
    length: int
    sequence: str

class AnalysisResult(BaseModel):
    """
    Represents the complete result of a signature analysis, including
    an AI-generated summary and a list of all found signatures.
    """
    summary: str
    signatures: List[Signature]