// app.js
document.addEventListener('DOMContentLoaded', function() {
    // Function to call the Python greeting functionality
    function displayGreeting() {
        const nameInput = document.getElementById('nameInput');
        const greetingDisplay = document.getElementById('greetingDisplay');
        
        if (nameInput && nameInput.value) {
            // In a real application, you might make an API call to the Python backend
            // For this example, we'll simulate it
            const name = nameInput.value;
            const currentTime = new Date().toLocaleTimeString('en-US', {
                year: 'numeric',
                month: 'numeric',
                day: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric',
                timeZoneName: 'short'
            });
            greetingDisplay.textContent = `Hello, ${name}! (at ${currentTime})`;
        } else {
            greetingDisplay.textContent = 'Please enter your name first.';
        }
    }
    
    // Add event listener to button if it exists
    const greetButton = document.getElementById('greetButton');
    if (greetButton) {
        greetButton.addEventListener('click', displayGreeting);
    }
    
    console.log('JavaScript initialized and ready to greet users!');
});

