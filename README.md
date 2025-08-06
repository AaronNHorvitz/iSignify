# iSignify: AI-Powered Microbial Signature Discovery

**iSignify is a rapid, AI-powered bioinformatics tool designed to pinpoint unique genetic 'fingerprints' in microbial genomes. It empowers scientists to accelerate diagnostics, enhance biosecurity, and monitor environmental health—all from a private, offline-first application.**

This project was developed for the **Google - The Gemma 3n Impact Challenge**.

---

## The Problem

Identifying unique DNA sequences that act as a definitive marker for a specific bacterium is a cornerstone of modern biology. However, this process is computationally intensive and traditionally requires significant bioinformatics expertise, access to high-performance computing clusters, and a multi-step workflow involving several different tools. This creates a barrier for researchers in the field, slowing down critical work in diagnostics and environmental science.

## Our Solution: iSignify

iSignify streamlines this complex process into a single, user-friendly web application. By leveraging an efficient, on-the-fly k-mer comparison algorithm and the interpretive power of Google's Gemma model, iSignify allows any scientist to upload raw genome files and receive a clear, actionable list of unique DNA signatures in minutes, not weeks.

The application runs locally, ensuring that sensitive genomic data remains private and secure, and is functional even without an internet connection—a critical feature for fieldwork and use in low-connectivity regions.

### Key Features
* **On-the-Fly Signature Discovery:** A robust Python backend compares a target genome against multiple background genomes to find unique sequences without the need for a pre-computed database.
* **Automated FASTA Pre-processing:** Seamlessly handles and merges complex multi-contig FASTA files into a compatible format automatically, simplifying the user's workflow.
* **AI-Powered Interpretation:** Uses a local Gemma model to translate complex numerical results into human-readable summaries, making the data immediately understandable.
* **Simple Web Interface:** An intuitive UI allows for easy parameter setting, file uploading, and visualization of results.
* **Downloadable Results:** Exports the final list of signatures to a CSV file for use in downstream applications like PCR primer design.
* **Private & Offline-First:** The entire analysis runs on the user's machine, ensuring data privacy and offline functionality.

---

## Real-World Impact & Future Applications

iSignify is more than a bioinformatics tool; it's a platform for tangible, positive change. By dramatically lowering the barrier to entry for genomic analysis, it can accelerate progress in numerous fields:

* **Personalized Medicine & Diagnostics:** Rapidly identify unique genetic markers for emerging pathogens from patient samples (e.g., blood tests), leading to faster diagnostic tests for diseases.
* **Biosecurity & Threat Detection:** Quickly generate signatures for known bioweapons or emerging biological threats, allowing for rapid field detection in the event of a strike.
* **Environmental Monitoring:** Detect the presence of specific bacteria (e.g., pollutants or beneficial microbes) in soil and water samples to monitor ecosystem health.
* **Food Safety & Agriculture:** Identify unique strains of foodborne pathogens like *Salmonella* or *E. coli* to trace outbreaks, or find markers for crop diseases.
* **Synthetic Biology:** Verify and track custom-engineered microbes by identifying their unique, synthetic DNA barcodes.

---

## Technology Stack
* **Backend:** Python 3.10+, FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **AI Model:** Google Gemma
* **Containerization:** Docker
* **Bioinformatics:** Biopython

---
---

## Getting Started & Live Demo

For a live demonstration of the application, please visit our deployment:
*[Link to your deployed application will go here]*

For detailed technical setup instructions, please see the [**Development Setup Guide**](docs/DEVELOPMENT_SETUP.md)[cite: 1].

### How to Test the Live Demo

To make testing easy, we've provided small sample genome files directly in this repository.

**1. Download the Sample Data:**
* Right-click and "Save Link As..." on each of the files below:
    * [**Sample_Target_Genome.fna**](https://github.com/AaronNHorvitz/iSignify/blob/main/sample_data/Sample_Target_B_amyloliquefaciens.fna)
    * [**Sample_Background_1.fna**](https://github.com/AaronNHorvitz/iSignify/blob/main/sample_data/Sample_Background_B_licheniformis.fna)

**2. Run the Analysis:**
* Go to our live demo URL.
* For **Target Genome**, upload the `Sample_Target_B_amyloliquefaciens.fna` file.
* For **Background Genomes**, select both `Sample_Background_B_licheniformis.fna` file. 
* Click **"Find Signatures"** to see the results!
---

## The Team

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

## Future Roadmap

This hackathon project serves as a robust proof-of-concept. Key planned features include **Automated PCR Primer Design**, **Clade-Based Optimization**, a **Parallel Processing Engine**, and a **Metagenomic Analysis Mode**.