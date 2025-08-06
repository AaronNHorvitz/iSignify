# FASTA File Preparation Guide for iSignify

**Author:** Charles Greenwald, PhD
***

This document outlines the required format for FASTA files used in the iSignify application and provides instructions for pre-processing raw genomic data.

## What is a FASTA File?

A FASTA file is a text-based file format widely used in bioinformatics to store biological sequence data, such as DNA, RNA, or protein sequences. Developed in the 1980s, it is simple, human-readable, and standardized, making it compatible with many bioinformatics tools for tasks like sequence alignment, genome assembly, and annotation. FASTA files are commonly used in databases like NCBI GenBank, UniProt, and Ensembl, and they can store single or multiple sequences.

Since FASTA files are plain text, you can open and edit them with any text editor. However, genomic data can be large, so they are often managed with specialized libraries like Biopython and tracked in version control with Git LFS for efficient storage.

### Structure of a FASTA File

A FASTA file consists of one or more sequences, each with two parts: a header line and the sequence data.

* **Header Line:**
    * Always starts with a greater-than symbol (`>`).
    * Immediately followed by a unique sequence identifier (e.g., `NC_009848.4`).
    * An optional description may follow the identifier, separated by a space.

* **Sequence Data:**
    * Starts on the line(s) after the header.
    * Uses single-letter codes for nucleotides or amino acids.
    * Can span multiple lines.

A "multi-FASTA" file contains multiple sequences, each starting with its own `>` header.

### What is a Contig?

A contig (short for "contiguous sequence") is a continuous, gap-free segment of DNA assembled from overlapping short reads produced during sequencing. In draft genomes, a complete genome may consist of multiple contigs, often stored in a multi-FASTA file where each contig has its own header.

## iSignify Pre-Processing Requirement

The iSignify program requires each FASTA file to contain **only one sequence with a single header** to ensure compatibility with its analysis pipeline. Genome sequences from draft assemblies are often in a multi-FASTA format (one header per contig), which will cause errors in the application.

### Recommended Steps for Processing

To make multi-contig FASTA files compatible with iSignify, you must merge the contigs into a single sequence with one header, using a string of ambiguous bases (`N`s) as spacers.


Check if the file is multi-FASTA by counting the number of headers:
```bash
grep -c -E '^>' data/Processed_FASTA_files/example.fna
```
If the count is greater than 1, the file needs processing.

**2. Merge Contigs**

You can use one of the following methods to merge the contigs.

**With Biopython (Python):**
First, install Biopython:

```bash
pip install biopython
```

Save this script as `merge_fasta.py:`


```python
from Bio import SeqIO
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

records = list(SeqIO.parse(input_file, "fasta"))
if len(records) > 1:
    # Use the first record as the base
    merged_seq = records[0].seq
    # Append subsequent records with a 100 'N' spacer
    for record in records[1:]:
        merged_seq += 'N' * 100 + record.seq
    records[0].seq = merged_seq
    SeqIO.write(records[0], output_file, "fasta")
    print(f"Merged {len(records)} contigs into {output_file}")
else:
    print("File already has one sequence; no changes needed.")
```

Run the script from your terminal:

```bash
python merge_fasta.py path/to/input.fna path/to/output.fna
```

**With AWK (Command-Line, No Dependencies):**

```bash
awk '
BEGIN { header = ""; seq = ""; spacer = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"; }
/^>/ {
    if (header == "") { header = $0; } # Keep only the first header
    next;
}
{ seq = seq ? seq spacer $0 : $0; }
END { if (header != "") { print header; print seq; } }
' path/to/input.fna > path/to/output.fna
```

3. Verify the Output

Confirm the processed file now has only one header:

```bash
grep -c -E '^>' path/to/output.fna
```

The expected output should be `1.`
