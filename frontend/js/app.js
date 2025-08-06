document.addEventListener('DOMContentLoaded', () => {

    // ... (keep all the other element selections) ...
    const form = document.getElementById('analysis-form');
    const submitButton = document.getElementById('submit-button');
    const resultsContainer = document.getElementById('results-container');
    const summaryDiv = document.getElementById('summary');
    const signaturesTable = document.getElementById('signatures-table');
    const loader = document.getElementById('loader');
    const downloadButton = document.getElementById('download-csv-button');
    const preprocessorToggle = document.getElementById('preprocessor-toggle'); // <-- NEW

    let currentSignatures = [];

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        // ... (keep the reset state logic) ...
        loader.classList.remove('hidden');
        resultsContainer.classList.add('hidden');
        downloadButton.classList.add('hidden');
        submitButton.disabled = true;
        submitButton.textContent = 'Analyzing...';
        currentSignatures = [];

        const formData = new FormData();
        formData.append('kmer_size', document.getElementById('kmer-size').value);
        formData.append('target_genome', document.getElementById('target-genome').files[0]);
        const backgroundFiles = document.getElementById('background-genomes').files;
        for (let i = 0; i < backgroundFiles.length; i++) {
            formData.append('background_genomes', backgroundFiles[i]);
        }
        
        // --- NEW: Add the toggle value to the form data ---
        formData.append('run_preprocessor', preprocessorToggle.checked);
        // ---------------------------------------------------

        try {
            const response = await fetch('https://aaronhhorvitz-isignify.hf.space/api/v1/analyze/', {
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
    
    // ... (keep the downloadButton event listener and display functions) ...
    downloadButton.addEventListener('click', () => {
        if (currentSignatures.length === 0) return;
        const headers = ['sequence_id', 'start', 'end', 'length', 'sequence'];
        let csvContent = headers.join(',') + '\n';
        currentSignatures.forEach(sig => {
            const row = [`"${sig.sequence_id}"`, sig.start, sig.end, sig.length, `"${sig.sequence}"`];
            csvContent += row.join(',') + '\n';
        });
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
        currentSignatures = data.signatures || [];
        let tableContent = 'ID\t\tStart\tEnd\tLength\tSequence\n';
        tableContent += '----------------------------------------------------------\n';
        if (currentSignatures.length > 0) {
            currentSignatures.forEach(sig => {
                tableContent += `${sig.sequence_id.substring(1, 15)}...\t${sig.start}\t${sig.end}\t${sig.length}\t${sig.sequence.substring(0, 20)}...\n`;
            });
            downloadButton.classList.remove('hidden');
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