Here is the existing task list. Let's add them in addition the UI changes were were going to make, and let's get this started. 
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
    - [ ] **4.2.1:** Add `biopython` to `requirements.txt` and install.
    - [ ] **4.2.2:** Implement merging logic from the guide in a new `preprocessor.py` module.
    - [ ] **4.2.3:** Refactor `AnalysisService` to use the new pre-processor.
    - [ ] **4.2.4:** Write unit tests for the pre-processor.
- [ ] **Task 4.3:** Finalize `Dockerfile` & Deploy Backend to Google Cloud Run.
- [ ] **Task 4.4:** Make final UI/CSS adjustments (Explanations, CSV Download, LLM Window).
- [ ] **Task 4.5:** Conduct final review with SME (Charles).

---
## Phase 5: Submission

- [ ] **Task 5.1:** Write the technical paper and add it to `docs/`.
- [ ] **Task 5.2:** Record and edit a compelling video demonstration.
- [ ] **Task 5.3:** Submit all materials to the Kaggle hackathon.
