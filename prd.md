# Product Requirements Document: Microbial Signature Identification

## 1. Overview

This document outlines the requirements for an application that identifies unique DNA signatures from microbial genomes. The system will compare a user-selected target genome against a group of background genomes to output specific sequences present only in the target. This functionality supports applications in diagnostics, microbial tracking, environmental monitoring, and biosurveillance.

---

## 2. Objective

* To build a local, efficient, and privacy-respecting tool for genomic comparison and the extraction of species- or strain-specific DNA sequences.
* To enable users with no bioinformatics expertise to upload genome files and receive meaningful, filterable results.
* To use the Gemma 3n model as a natural language and reasoning engine to generate human-readable summaries, assist with data filtering, and suggest interpretations.

---

## 3. Functional Requirements

### Genome Upload and Comparison
* The system must accept DNA sequence files in standard formats (e.g., `.fna`, `.fa`).
* Users must be able to select one genome as the **target** and one or more genomes as the **background** set.
* The interface will provide an option for users to define the `k-mer` size or a uniqueness threshold for the analysis.

### Signature Identification
* The application will analyze the target genome against the background set to detect and extract unique genomic regions.
* The system will merge overlapping or adjacent unique `k-mers` into longer, contiguous signature regions.
* The primary output for each signature will include its start and end positions, length, and the DNA sequence itself.

### Natural Language Explanation
* The integrated Gemma 3n model will generate a high-level summary of the results (e.g., "37 unique regions were identified, ranging from 50 to 150 bp in length.").
* The system will support natural language queries for filtering and exploring the results (e.g., “Show me the longest signature,” or “Which genes are covered by signatures?”).

### Annotation Overlay (Optional)
* If a gene annotation file (e.g., `.gff`, `.gbk`) is provided, the application will map the detected signatures to known gene regions.
* The output will specify whether a signature is located within a coding sequence (CDS) or an intergenic region.

### Filtering and Data Export
* Results will be displayed in a searchable and sortable table.
* Users will be able to filter results by sequence length, GC content, or the presence of a specific motif.
* The application must provide functionality to export filtered results in `.tsv` or `.fasta` format.

---

## 4. Non-Functional Requirements

* **Offline Capability:** The application must be capable of running on a local device, utilizing a local instance of the Gemma 3n inference engine.
* **Performance:** The software should be scalable enough to handle genome sizes ranging from bacteria to small eukaryotes.
* **Resource Efficiency:** The tool must be lightweight enough to run on systems with 4 GB of RAM or less.
* **Usability:** The application will feature a user-friendly web or graphical user interface (GUI) suitable for non-technical users.

---

## 5. Use Cases

### Research and Diagnostics
* Identification of species- or strain-specific markers for the design of diagnostic PCR primers and probes.

### Environmental Microbiology
* Discovery of unique signatures to enable the detection of specific bacteria within complex metagenomic samples.

### Synthetic Biology
* Design of synthetic control strains containing unique, trackable DNA barcodes.

### Biosecurity
* Generation of specific exclusion filters to improve the accuracy of biothreat identification pipelines.