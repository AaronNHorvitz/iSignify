# Technical Writeup: iSignify

**A Rapid, AI-Powered Application for Microbial Signature Discovery**

**Team:**
* **Charles Greenwald, PhD, MBA** - *Subject Matter Expert*
* **Aaron Horvitz, M.S.** - *Developer & Data Scientist*

**Project for the Google - The Gemma 3n Impact Challenge**

---

### Quick Links

* **Live Demo Application:** **[https://fanciful-youtiao-87cf94.netlify.app/](https://fanciful-youtiao-87cf94.netlify.app/)**
* **Video Overview:** **[Link to YouTube Video Overview](https://www.youtube.com/watch?v=UD_7MTGaDJ4)**
* **Main GitHub Repository (README):** **[https://github.com/AaronNHorvitz/iSignify](https://github.com/AaronNHorvitz/iSignify)**
* **Sample Data Files:**
    * [**Sample\_Target\_Genome.fna**](https://github.com/AaronNHorvitz/iSignify/blob/main/sample_data/Sample_Target_B_amyloliquefaciens.fna)
    * [**Sample\_Background\_1.fna**](https://github.com/AaronNHorvitz/iSignify/blob/main/sample_data/Sample_Background_B_licheniformis.fna)


---

## 1. Abstract

Identifying unique DNA sequences that definitively mark a specific microorganism is a foundational challenge in modern biology. This process is computationally intensive and has traditionally been inaccessible to researchers without specialized bioinformatics training. iSignify is a rapid, AI-powered, and privacy-respecting application designed to solve this problem. By integrating an efficient on-the-fly comparison algorithm with the interpretive power of Google's Gemma model, iSignify empowers any scientist to discover unique DNA signatures in minutes, dramatically accelerating research in diagnostics, biosecurity, and environmental health.

---

## 2. Introduction: The Problem

The ability to pinpoint a unique genetic "fingerprint" for a bacterium or virus is critical for a vast range of applications, from diagnosing infectious diseases to monitoring for biological threats. However, the workflow to find these signatures is a significant bottleneck. It typically involves:
* Access to high-performance computing clusters.
* Expertise in complex command-line bioinformatics tools.
* A multi-step, multi-day process of sequence alignment, data filtering, and interpretation.

This high barrier to entry slows down innovation and limits the ability of researchers in the field to rapidly respond to emerging challenges. Our goal was to create a tool that would democratize this powerful capability.

---

## 3. Our Solution: iSignify

iSignify streamlines this entire complex workflow into a single, intuitive web application. It is built on the principle of being **private, offline-first, and user-friendly**, aligning perfectly with the capabilities of the Gemma model.

A user can simply upload their raw target and background genome files, set a single parameter, and receive a clear, actionable list of unique DNA signatures. The application's core logic runs locally, and the integrated Gemma model provides a human-readable summary of the results, making complex genomic data immediately understandable.

### Key Features & Innovations

* **On-the-Fly Signature Discovery:** A robust Python backend compares a target genome against multiple background genomes to find unique sequences without the need for a pre-computed database.
* **Automated FASTA Pre-processing:** The application seamlessly handles and merges complex, multi-contig FASTA files into a compatible single-sequence format automatically, removing a common and error-prone manual step for the user.
* **AI-Powered Interpretation:** iSignify uses a local Gemma model to translate the quantitative results of the analysis into a qualitative, human-readable summary, bridging the gap between raw data and scientific insight.
* **Downloadable & Actionable Results:** The application provides the final list of signatures in a downloadable CSV format, ready for use in downstream applications like the design of diagnostic PCR primers.

---

## 4. System Architecture

iSignify is a full-stack web application designed with a clean separation of concerns between the frontend, backend, and the core bioinformatics engine.

### Technology Stack
* **Backend:** Python 3.10+, FastAPI
* **Frontend:** HTML, CSS, JavaScript (no framework)
* **AI Model:** Google Gemma
* **Containerization:** Docker
* **Bioinformatics:** Biopython

### Architectural Overview

The project is organized into distinct components, as detailed in our [**File Architecture Guide**](https://github.com/AaronNHorvitz/iSignify/blob/main/docs/FILE_ARCHITECTURE.md).

* **Frontend:** A simple, static web interface built with HTML, CSS, and JavaScript that allows users to upload files and view results. It communicates with the backend via a REST API.
* **Backend API (`FastAPI`):** A robust API layer that handles file uploads, validates inputs, and orchestrates the analysis by calling the service layer.
* **Service Layer:** The `AnalysisService` acts as the application's central nervous system. It manages the entire workflow: receiving files from the API, passing them to the pre-processor, sending the cleaned data to the core engine, passing the results to the AI model, and finally formatting the response.
* **Core Logic (The Engine):**
    * `FastaPreprocessor`: An automated data cleaning module that uses the `Biopython` library to merge multi-contig FASTA files.
    * `SequenceParser`: A simple, efficient parser for reading FASTA files.
    * `SignatureFinder`: The heart of the application. It uses an efficient, set-based k-mer comparison algorithm to perform the signature discovery.

---

## 5. The Data Pre-processing Workflow

A key technical challenge in bioinformatics is handling the variability of input data. Draft genomes are often delivered in a "multi-FASTA" format, where a single genome is split into many separate sequences (contigs). Our application was designed to handle this complexity automatically.

As detailed in our [**FASTA File Preparation Guide for iSignify**](https://github.com/AaronNHorvitz/iSignify/blob/main/docs/FASTA_PROCESSING_INSTRUCTIONS.md) (authored by our Subject Matter Expert, Charles Greenwald, PhD), our `FastaPreprocessor` module uses the `Biopython` library to automatically detect and merge these multi-contig files, inserting a standardized spacer of 100 'N's between each contig. This creates a single, continuous sequence that is compatible with our analysis engine. This automated step is a critical feature that significantly improves the application's usability for researchers.

---

## 6. Real-World Impact & Future Applications

iSignify is a platform for tangible, positive change. By dramatically lowering the barrier to entry for genomic analysis, it can accelerate progress in:

* **Personalized Medicine & Diagnostics:** Rapidly identify unique genetic markers for emerging pathogens from patient samples (e.g., blood tests), leading to faster diagnostic tests for diseases.
* **Biosecurity & Threat Detection:** Quickly generate signatures for known bioweapons or emerging biological threats, allowing for rapid field detection in the event of a strike.
* **Environmental Monitoring:** Detect the presence of specific bacteria (e.g., pollutants or beneficial microbes) in soil and water samples to monitor ecosystem health.

## 7. Future Roadmap

This hackathon project serves as a robust proof-of-concept. Key planned features to evolve iSignify into a production-ready tool include:

* **Automated PCR Primer Design:** Integrate an engine like Primer3 to automatically design and validate optimal PCR primers for any given signature.
* **Optimization:** Implement a UI and backend logic to allow users to group background genomes into "clades" and intelligently compare against a single representative from each, dramatically improving performance for large-scale analyses.
* **Parallel Processing Engine:** Refactor the core algorithm to use Python's `multiprocessing` module, allowing the analysis to run in parallel across all available CPU cores.