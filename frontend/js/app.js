// Wait for the entire HTML document to be loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // Select the important elements from the HTML
    const form = document.getElementById('analysis-form');
    const submitButton = document.getElementById('submit-button');
    const resultsContainer = document.getElementById('results-container');
    const summaryDiv = document.getElementById('summary');
    const signaturesTable = document.getElementById('signatures-table');
    const loader = document.getElementById('loader');

    // Add an event listener to the form for when it is submitted
    form.addEventListener('submit', async (event) => {
        // Prevent the default browser action of reloading the page on submit
        event.preventDefault();

        // Show the loader and hide previous results
        loader.classList.remove('hidden');
        resultsContainer.classList.add('hidden');
        submitButton.disabled = true;
        submitButton.textContent = 'Analyzing...';

        // Create a FormData object to package our form data and files
        const formData = new FormData();

        // Get the values from the form inputs
        const kmerSize = document.getElementById('kmer-size').value;
        const targetFile = document.getElementById('target-genome').files[0];
        const backgroundFiles = document.getElementById('background-genomes').files;

        // Add the data to our FormData object
        formData.append('kmer_size', kmerSize);
        formData.append('target_genome', targetFile);
        for (let i = 0; i < backgroundFiles.length; i++) {
            formData.append('background_genomes', backgroundFiles[i]);
        }

        try {
            // Use the fetch API to send the data to our backend endpoint
            const response = await fetch('http://localhost:8000/api/v1/analyze/', {
                method: 'POST',
                body: formData,
            });

            // Check if the response was successful
            if (response.ok) {
                const data = await response.json();
                displayResults(data);
            } else {
                // If the server returned an error, display it
                const errorData = await response.json();
                displayError(errorData.detail || 'An unknown error occurred.');
            }
        } catch (error) {
            // Handle network errors
            displayError('A network error occurred. Is the backend server running?');
            console.error('Error:', error);
        } finally {
            // Hide the loader and re-enable the button
            loader.classList.add('hidden');
            submitButton.disabled = false;
            submitButton.textContent = 'Find Signatures';
        }
    });

    function displayResults(data) {
        // Display the AI-generated summary
        summaryDiv.textContent = data.summary;

        // Format the signature data for display
        let tableContent = 'ID\t\tStart\tEnd\tLength\tSequence\n';
        tableContent += '----------------------------------------------------------\n';
        if (data.signatures && data.signatures.length > 0) {
            data.signatures.forEach(sig => {
                tableContent += `${sig.sequence_id.substring(1, 15)}...\t${sig.start}\t${sig.end}\t${sig.length}\t${sig.sequence.substring(0, 20)}...\n`;
            });
        } else {
            tableContent += 'No unique signatures found.';
        }
        signaturesTable.textContent = tableContent;

        // Show the results container
        resultsContainer.classList.remove('hidden');
    }

    function displayError(message) {
        summaryDiv.textContent = `Error: ${message}`;
        signaturesTable.textContent = '';
        resultsContainer.classList.remove('hidden');
    }
});