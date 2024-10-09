// Function to calculate age based on birthdate input
function calculateAge(birthday) {
    const birthDate = new Date(birthday);
    const today = new Date();
    
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDifference = today.getMonth() - birthDate.getMonth();

    // Check if the birthday hasn't occurred yet this year
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }

    return age;
}

// Function to trigger confetti animation
function launchConfetti() {
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
}

// Event listener for form submission
document.getElementById('age-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const birthday = document.getElementById('birthday').value;
    if (birthday) {
        const age = calculateAge(birthday);
        document.getElementById('result').innerHTML = `You are ${age} years old.`;

        // Trigger the confetti animation
        launchConfetti();
    } else {
        document.getElementById('result').innerHTML = `Please enter a valid date.`;
    }
});
