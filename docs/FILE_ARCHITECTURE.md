# Project File Architecture

This document provides an overview of the iSignify project's file and directory structure.

## Directory Tree

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
│       ├── test_preprocessor.py
│       ├── test_sequence_parser.py
│       └── test_signature_finder.py
│
├── docs/
│   ├── DEVELOPMENT_SETUP.md
│   ├── FASTA_PROCESSING_INSTRUCTIONS.md
│   ├── FILE_ARCHITECTURE.md
│   ├── PRD.md
│   └── insignia_2009_paper.pdf
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

## Component Descriptions

* **`/` (Root Directory):** Contains all top-level project configuration files, including the main `README.md`, the `Dockerfile` for containerization, and Python dependency management (`requirements.txt`).

* **`/backend`:** Contains all the Python server-side application code.
    * **`/backend/src`:** The main, installable Python package for the application, following the standard `src` layout.
        * **`/api`:** Defines the FastAPI endpoints.
        * **`/core`:** Contains the core, standalone bioinformatics logic (parsing, signature finding, pre-processing).
        * **`/models`:** Contains the Pydantic data schemas for API responses.
        * **`/services`:** The orchestration layer that connects the API to the core logic.
    * **`/backend/tests`:** Contains all the unit tests for the backend code.

* **`/frontend`:** Contains all the client-side code for the user interface, including the `index.html`, `style.css`, and `app.js` files.

* **`/data`:** Contains sample and processed genome data files. Large files in this directory are tracked using Git LFS, while local-only test data is ignored by `.gitignore`.

* **`/docs`:** Contains all project documentation, including the Product Requirements Document (PRD), detailed developer setup guides, and the final technical writeup.
