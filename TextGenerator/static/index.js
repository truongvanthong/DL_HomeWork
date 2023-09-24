document.addEventListener("DOMContentLoaded", function() {
    const textForm = document.getElementById("textForm");
    const inputText = document.getElementById("inputText");
    const outputLength = document.getElementById("outputLength");
    const outputText = document.getElementById("outputText");

    textForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const inputData = {
            text: inputText.value,
            length: parseInt(outputLength.value)
        };

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
            // Update the output text with the response from the server
            outputText.textContent = data.output_text;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});