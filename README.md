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
│   │   │   ├── __init__.py
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
├── .gitattributes
├── TASKS.md
└── README.md
```
## 3. How to Contribute Large Data Files

This project uses Git LFS (Large File Storage) to manage large genome files. To contribute data files, please follow these steps:

**1. Install Git LFS (One-Time Setup)**

If you don't have it already, you need to install the Git LFS extension on your computer. You can download it from the official website:
* [https://git-lfs.github.com](https://git-lfs.github.com)

After installing, run the following command in your terminal to initialize it:
```bash
git lfs install
```

**2. Add and Commit Files**
The repository is already configured to know which files to track with LFS. You can now add, commit, and push large FASTA files using standard Git commands.

- Place the files in the `data/FASTA_files/ directory`.

- Run the standard git commands:

```bash
git add data/FASTA_files/your_large_file.fna
git commit -m "Add new genome file for testing"
git push
```
Git LFS will automatically handle the upload process correctly.

## 4. Backend Class Design

**`backend/src/core/sequence_parser.py`**
```python
class SequenceParser:
    def parse(self, file_path: str) -> dict[str, str]:
        """Reads a FASTA file and returns a dictionary of headers to sequences."""
```

**`backend/src/core/signature_finder.py`**
```python
class SignatureFinder:
    def __init__(self, kmer_size: int):
        """Initializes the finder with a k-mer size."""
        pass

    def find_unique_signatures(self, target_sequences: dict, background_sequences: dict) -> list[dict]:
        """Finds unique, merged signature regions in the target sequences."""
        pass
```
## 5. Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/AaronNHorvitz/iSignify.git
cd iSignify
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

## 6. Running Tests

You can run the unit tests using two methods:

### A. Locally (Recommended for Development)

Ensure you have created and activated a virtual environment and installed the dependencies as described in the "Getting Started" section.

1.  Navigate to the `backend/` directory:
    ```bash
    cd backend
    ```
2.  Run pytest:
    ```bash
    pytest
    ```

### B. Using Docker (Ensures a Clean Environment)

This method runs the tests inside the same container environment defined in the `Dockerfile`.

1.  Make sure your Docker Desktop is running.
2.  From the project's root directory (`iSignify/`), build the Docker image:
    ```bash
    docker build -t isignify-app .
    ```
3.  Run the tests inside a temporary container:
    ```bash
    docker run --rm isignify-app pytest
    ```
* `--rm` automatically removes the container after the tests are finished.
* `pytest` overrides the default `CMD` in the Dockerfile, running the test suite instead of the web server.