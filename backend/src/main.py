from fastapi import FastAPI
from src.api.v1 import analysis_routes

# Create an instance of the FastAPI class
app = FastAPI(
    title="iSignify API",
    description="API for identifying unique microbial DNA signatures.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the iSignify API!"}

# Include the analysis router in our main application
app.include_router(analysis_routes.router, prefix="/api/v1")
