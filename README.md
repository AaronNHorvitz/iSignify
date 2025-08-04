# Microbial Signature Identification App (iSignify)

This project is a local, privacy-respecting application that identifies unique DNA signatures from microbial genomes. It compares a target genome against a background set and uses the Gemma 3n model to provide human-readable summaries of the results.

## 1. Project Roadmap

The project will be executed in several key phases. For a detailed, actionable checklist of all tasks, please see the `TASKS.md` file in the project repository.

* **Phase 1:** Backend Core Logic Development
* **Phase 2:** Backend API Implementation
* **Phase 3:** Frontend UI Construction
* **Phase 4:** AI Model Integration and Finalization
* **Phase 5:** Final Review and Hackathon Submission

---

## 2. Architecture & Design

### Technology Stack
* **Backend:** Python 3.10+, FastAPI
* **Frontend:** HTML, CSS, JavaScript (no framework)
* **AI Model:** Gemma 3n (running locally)
* **Containerization:** Docker

### File Structure

```
iSignify/
│
|── data/
│   └── FASTA_files
|
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── analysis_routes.py
│   │   ├── core/
│   │   │   ├── sequence_parser.py
│   │   │   └── signature_finder.py
│   │   ├── models/
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   └── analysis_service.py
│   │   └── main.py
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_signature_finder.py
│
├── docs/
│   ├── PRD.md
│   └── insignia_2009_paper.pdf
│
├── frontend/
│   ├── index.html
│   └── ...
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── TASKS.md
└── README.md
```

## Backend Class Design

**`app/core/sequence_parser.py`**
```python
class SequenceParser:
    def parse(self, file_path: str) -> dict[str, str]:
        """Reads a FASTA file and returns a dictionary of headers to sequences."""
```

**`app/core/signature_finder.py`**
```python
class SignatureFinder:
    def __init__(self, kmer_size: int):
        """Initializes the finder with a k-mer size."""
        pass

    def find_unique_signatures(self, target_sequences: dict, background_sequences: dict) -> list[dict]:
        """Finds unique, merged signature regions in the target sequences."""
        pass
```
## 3. Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/AaronNHorvitz/iSignify.git
cd gemma-signature-app
```

### 2. Set up the backend:
```bash
# Install dependencies from the root directory
pip install -r requirements.txt
```

### 3. Run the backend server:
```bash
# Navigate into the backend folder
cd backend

# Run the server from within the backend directory
uvicorn src.main:app --reload
```

### 4. Open the frontend:
* Navigate to the `frontend/` directory and open `index.html` in your web browser.

