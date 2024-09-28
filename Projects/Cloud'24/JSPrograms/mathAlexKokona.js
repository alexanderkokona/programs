// Accessing command-line arguments
const args = process.argv.slice(2);

// Extracting numbers and the operation
const num1 = parseFloat(args[0]);
const operation = args[1];
const num2 = parseFloat(args[2]);

// Function to perform the math operation
function performOperation(num1, operation, num2) {
    switch (operation) {
        case 'add':
            return `${num1} + ${num2} = ${num1 + num2}`;
        case 'subtract':
            return `${num1} - ${num2} = ${num1 - num2}`;
        case 'multiply':
            return `${num1} * ${num2} = ${num1 * num2}`;
        case 'divide':
            if (num2 === 0) return 'Error: Division by zero is not allowed.';
            return `${num1} / ${num2} = ${num1 / num2}`;
        case 'exponent':
            return `${num1} ^ ${num2} = ${Math.pow(num1, num2)}`;
        default:
            return 'Error: Invalid operation. Supported operations are add, subtract, multiply, divide, exponent.';
    }
}

// Checking if input is valid
if (isNaN(num1) || isNaN(num2)) {
    console.log('Error: Please provide two valid numbers.');
} else {
    console.log(performOperation(num1, operation, num2));
}
