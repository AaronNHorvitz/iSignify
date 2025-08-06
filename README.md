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
│   ├── FASTA_files
│   └── Processed_FASTA_files
|
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       └── analysis_routes.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── preprocessor.py
│   │   │   ├── sequence_parser.py
│   │   │   └── signature_finder.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── analysis_service.py
│   │   └── main.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── test_sequence_parser.py
│       └── test_signature_finder.py
│
├── docs/
│   ├── DEVELOPMENT_SETUP.md
│   ├── FASTA_Processing_instructions.md
│   ├── insignia_2009_paper.pdf
│   └── prd.md
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
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

### 2.  Set up your local environment:
For a detailed, step-by-step guide on setting up your Python virtual environment and installing dependencies, please see the [Development Setup Guide](https://github.com/AaronNHorvitz/iSignify/blob/main/docs/DEVELOPMENT_SETUP.md)

*Note: To enable the AI summary feature, you will need to complete the additional Hugging Face authentication steps at the end of the setup guide.*

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

## 7. The Team

* **Charles Greenwald, PhD, MBA** - *Subject Matter Expert*
    * Vice President, Global Biological Platform at NCH Corporation. 
    * PhD in Genetics, Texas A&M University

* **Aaron Horvitz** - *Developer & Data Scientist*
    * Statistician (Data Scientist) at RAAS (Research Analytics and Applied Statistics) at the Internal Revenue Service
    * MS Analytics, Texas A&M University
    * MS Statistical Data Science, Texas A&M University (In Progress)

### Acknowledgments

This project's code was developed by Aaron Horvitz, with significant pairing and assistance from Google's Gemini model.

---

## Future Roadmap (Post-Hackathon)

This hackathon project serves as a robust proof-of-concept. The following features are planned to evolve iSignify into a production-ready tool for researchers.

* **Automated PCR Primer Design:**
    Integrate a bioinformatics engine like Primer3 to automatically design and validate optimal PCR primers for any given signature, complete with data on melting temperatures, GC content, and potential hairpins.

* **Clade-Based Optimization:**
    To dramatically improve performance for large-scale analyses, a UI and backend logic will be developed to allow users to group background genomes into "clades" (e.g., by genus or family). The analysis will then intelligently compare a target against a single representative from each clade, reducing computation time exponentially.

* **Parallel Processing Engine:**
    The core signature finding algorithm will be refactored to use Python's `multiprocessing` module. This will allow the analysis to run in parallel across all available CPU cores, providing a significant speedup for large genomes.

* **Metagenomic Analysis Mode:**
    A future research goal is to develop a new analysis mode capable of identifying novel, unknown organisms within mixed-environmental (metagenomic) samples by comparing them against public databases.
