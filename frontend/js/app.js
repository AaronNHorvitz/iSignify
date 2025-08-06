document.addEventListener('DOMContentLoaded', () => {

    // Select all elements
    const form = document.getElementById('analysis-form');
    const submitButton = document.getElementById('submit-button');
    const resultsContainer = document.getElementById('results-container');
    const summaryDiv = document.getElementById('summary');
    const signaturesTable = document.getElementById('signatures-table');
    const loader = document.getElementById('loader');
    const downloadButton = document.getElementById('download-csv-button'); // <-- NEW

    // Store results globally to make them accessible for download
    let currentSignatures = []; // <-- NEW

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        // Reset state
        loader.classList.remove('hidden');
        resultsContainer.classList.add('hidden');
        downloadButton.classList.add('hidden'); // <-- NEW
        submitButton.disabled = true;
        submitButton.textContent = 'Analyzing...';
        currentSignatures = []; // <-- NEW: Clear previous results

        const formData = new FormData();
        formData.append('kmer_size', document.getElementById('kmer-size').value);
        formData.append('target_genome', document.getElementById('target-genome').files[0]);
        const backgroundFiles = document.getElementById('background-genomes').files;
        for (let i = 0; i < backgroundFiles.length; i++) {
            formData.append('background_genomes', backgroundFiles[i]);
        }

        try {
            const response = await fetch('http://localhost:8000/api/v1/analyze/', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                displayResults(data);
            } else {
                const errorData = await response.json();
                displayError(errorData.detail || 'An unknown error occurred.');
            }
        } catch (error) {
            displayError('A network error occurred. Is the backend server running?');
            console.error('Error:', error);
        } finally {
            loader.classList.add('hidden');
            submitButton.disabled = false;
            submitButton.textContent = 'Find Signatures';
        }
    });

    // --- NEW: Event listener for the download button ---
    downloadButton.addEventListener('click', () => {
        if (currentSignatures.length === 0) return;

        // Define CSV headers
        const headers = ['sequence_id', 'start', 'end', 'length', 'sequence'];
        let csvContent = headers.join(',') + '\n';

        // Loop through the signature data and add to the CSV string
        currentSignatures.forEach(sig => {
            const row = [
                `"${sig.sequence_id}"`,
                sig.start,
                sig.end,
                sig.length,
                `"${sig.sequence}"`
            ];
            csvContent += row.join(',') + '\n';
        });

        // Create a downloadable file from the CSV string
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        if (link.download !== undefined) {
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', 'isignify_results.csv');
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    });

    function displayResults(data) {
        summaryDiv.textContent = data.summary;
        
        currentSignatures = data.signatures || []; // <-- NEW: Store results

        let tableContent = 'ID\t\tStart\tEnd\tLength\tSequence\n';
        tableContent += '----------------------------------------------------------\n';
        if (currentSignatures.length > 0) {
            currentSignatures.forEach(sig => {
                tableContent += `${sig.sequence_id.substring(1, 15)}...\t${sig.start}\t${sig.end}\t${sig.length}\t${sig.sequence.substring(0, 20)}...\n`;
            });
            downloadButton.classList.remove('hidden'); // <-- NEW: Show download button
        } else {
            tableContent += 'No unique signatures found.';
        }
        signaturesTable.textContent = tableContent;
        resultsContainer.classList.remove('hidden');
    }

    function displayError(message) {
        summaryDiv.textContent = `Error: ${message}`;
        signaturesTable.textContent = '';
        resultsContainer.classList.remove('hidden');
    }
});