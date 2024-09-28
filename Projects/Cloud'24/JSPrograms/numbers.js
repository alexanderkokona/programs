// Function to add two numbers
function addNumbers(a, b) {
    return a + b;
}

// Get the arguments from the command line
const args = process.argv.slice(2);

// Ensure two numbers are passed as arguments
if (args.length < 2) {
    console.log("Please provide two numbers as arguments.");
    process.exit(1);
}

// Convert the arguments to numbers
const num1 = parseFloat(args[0]);
const num2 = parseFloat(args[1]);

// Check if both arguments are valid numbers
if (isNaN(num1) || isNaN(num2)) {
    console.log("Both arguments must be valid numbers.");
    process.exit(1);
}

// Call the function and display the result
const result = addNumbers(num1, num2);
console.log(`The result of adding ${num1} and ${num2} is: ${result}`);
