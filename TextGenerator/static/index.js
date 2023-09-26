document.addEventListener("DOMContentLoaded", function() {
    const textForm = document.getElementById("textForm");
    const inputText = document.getElementById("inputText");
    const outputLength = document.getElementById("outputLength");
    const outputText = document.getElementById("outputText");
    const loading = document.getElementById("loading");

    textForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const inputData = {
            text: inputText.value,
            length: parseInt(outputLength.value)
        };
        
        // Show the loading screen
        loading.style.display = "block";
        outputText.textContent = ""; // Clear previous output

        // Send a POST request to the '/process' route
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputData)
        })
        .then(response => response.json())
        .then(data => {
            // Hide the loading screen and update the output text with the response from the server
            loading.style.display = "none";
            outputText.textContent = data.output_text;
        })
        .catch(error => {
            console.error('Error:', error);
            // Hide the loading screen in case of an error
            loading.style.display = "none";
        });
    });
});