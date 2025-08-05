from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import analysis_routes

# Create an instance of the FastAPI class
app = FastAPI(
    title="iSignify API",
    description="API for identifying unique microbial DNA signatures.",
    version="0.1.0",
)

# --- NEW: Add CORS Middleware ---
# This allows your frontend (running on a different origin) to communicate with your backend.
origins = [
    # For development, allowing all origins is the simplest.
    # A 'null' origin is what browsers often use for requests from local files (file:///).
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# -----------------------------

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the iSignify API!"}

# Include the analysis router in our main application
app.include_router(analysis_routes.router, prefix="/api/v1")