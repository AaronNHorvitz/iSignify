# Project Tasks & Checklist

This document tracks the detailed tasks for the project. Check off items as they are completed.

---

## ✅ Phase 1: Backend Core Logic

- [ ] **Task 1.1:** Implement the `SequenceParser` class in `app/core/sequence_parser.py` to read and parse FASTA files.
- [ ] **Task 1.2:** Implement the `SignatureFinder` class in `app/core/signature_finder.py`, including the `__init__` and `_generate_kmers` methods.
- [ ] **Task 1.3:** Implement the main `find_unique_signatures` method, including the logic to merge adjacent k-mers into longer regions.
- [ ] **Task 1.4:** Write basic unit tests in the `tests/` directory for the `SignatureFinder` to validate the core algorithm.

---

## ✅ Phase 2: Backend API

- [ ] **Task 2.1:** Set up the basic FastAPI application instance in `backend/main.py`.
- [ ] **Task 2.2:** Define the Pydantic models for API requests and responses in `app/models/schemas.py`.
- [ ] **Task 2.3:** Build the API endpoint in `app/api/v1/analysis_routes.py` to handle file uploads and form data.
- [ ] **Task 2.4:** Implement the `AnalysisService` in `app/services/analysis_service.py` to connect the API endpoint to the core signature finding logic.

---

## ✅ Phase 3: Frontend UI

- [ ] **Task 3.1:** Create the `index.html` file with the necessary forms for file uploads, a `k-mer` size input, and a display area for results.
- [ ] **Task 3.2:** Write the JavaScript logic in `frontend/js/app.js` to handle form submission via the `fetch` API and to dynamically render results returned from the backend.
- [ ] **Task 3.3:** Add basic styling in `frontend/css/style.css` to make the application clean and user-friendly.

---

## ✅ Phase 4: AI Integration & Finalization

- [ ] **Task 4.1:** Integrate the Gemma 3n model into the `AnalysisService`. The service should pass the signature results to the model and get back a human-readable summary.
- [ ] **Task 4.2:** Finalize and test the `Dockerfile` to ensure the backend can be built and run successfully as a container.
- [ ] **Task 4.3:** (Optional) Create a `docker-compose.yml` file to make running the full stack (backend and a simple frontend server) easier during development.

---

## ✅ Phase 5: Submission

- [ ] **Task 5.1:** Record a compelling video demonstration of the working application, walking through a clear use case.
- [ ] **Task 5.2:** Write the final project description and documentation required for the Kaggle submission.
- [ ] **Task 5.3:** Submit the project to the hackathon.