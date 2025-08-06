# Project Tasks & Checklist

This document tracks the detailed tasks for the project. Check off items as they are completed.

---

## Phase 1: Backend Core Logic (Completed)

- [x] **Task 1.1:** Implement the `SequenceParser` class.
- [x] **Task 1.2:** Implement the `SignatureFinder` class skeleton.
- [x] **Task 1.3:** Implement the main `find_unique_signatures` method.
- [x] **Task 1.4:** Write and pass all unit tests for the core logic.

---

## Phase 2: Backend API (Completed)

- [x] **Task 2.1:** Set up the basic FastAPI application instance.
- [x] **Task 2.2:** Define the Pydantic models for API responses.
- [x] **Task 2.3:** Build the API endpoint for file uploads.
- [x] **Task 2.4:** Implement the `AnalysisService` to connect the API and core logic.

---

## Phase 3: Frontend UI (Completed)

- [x] **Task 3.1:** Create the `index.html` file.
- [x] **Task 3.2:** Write the JavaScript logic to call the API.
- [x] **Task 3.3:** Add basic styling with `style.css`.

---

## Phase 4: Finalization & Deployment

- [x] **Task 4.1:** Integrate the Gemma model into the `AnalysisService`.
- [ ] **Task 4.2:** Implement Automated FASTA Pre-processing:
    - [x] **4.2.1:** Add `biopython` to `requirements.txt` and install.
    - [x] **4.2.2:** Implement merging logic in a new `preprocessor.py` module.
    - [ ] **4.2.3:** Refactor `AnalysisService` to use the new pre-processor.
    - [x] **4.2.4:** Write and pass unit tests for the pre-processor.
- [ ] **Task 4.3:** Make final UI/CSS adjustments:
    - [ ] **4.3.1:** Add explanatory text to the UI to guide users/judges.
    - [ ] **4.3.2:** Implement a "Download as CSV" button for the results table.
    - [ ] **4.3.3:** Adjust CSS to make the LLM summary window larger and scrollable.
- [ ] **Task 4.4:** Conduct final review with SME (Charles).
- [ ] **Task 4.5:** Finalize `Dockerfile` & Deploy Backend to Google Cloud Run.

---
## Phase 5: Submission

- [ ] **Task 5.1:** Write the technical paper and add it to `docs/`.
- [ ] **Task 5.2:** Record and edit a compelling video demonstration.
- [ ] **Task 5.3:** Submit all materials to the Kaggle hackathon.
