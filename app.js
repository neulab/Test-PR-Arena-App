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
            
            // Format date with timezone information
            const now = new Date();
            const options = {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                timeZoneName: 'short'
            };
            const currentTime = now.toLocaleString('en-US', options);
            
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

