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
            return 'Error: Invalid operation.';
    }
}

function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const operation = document.getElementById('operation').value;
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').innerText = 'Error: Please provide two valid numbers.';
    } else {
        const result = performOperation(num1, operation, num2);
        document.getElementById('result').innerText = result;
    }
}
