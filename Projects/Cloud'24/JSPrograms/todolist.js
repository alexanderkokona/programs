const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// File to store the to-do list
const FILE_PATH = path.join(__dirname, 'todoList.json');

// In-memory to-do list
let todoList = [];

// Priority order for sorting
const priorityOrder = {
    high: 1,
    medium: 2,
    low: 3
};

// Load the to-do list from the file
function loadTodoList() {
    if (fs.existsSync(FILE_PATH)) {
        const data = fs.readFileSync(FILE_PATH, 'utf8');
        todoList = JSON.parse(data);
        console.log("To-do list loaded from file.");
    } else {
        console.log("No saved to-do list found. Starting fresh.");
    }
}

// Save the to-do list to the file
function saveTodoList() {
    fs.writeFileSync(FILE_PATH, JSON.stringify(todoList, null, 2));
    console.log("To-do list saved to file.");
}

// Sort the to-do list by priority (high -> medium -> low)
function sortTodoList() {
    todoList.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);
}

// Display the to-do list with priorities
function displayTodoList() {
    sortTodoList();  // Sort the list before displaying
    console.log("\nYour To-Do List (sorted by priority):");
    if (todoList.length === 0) {
        console.log("(Empty)");
    } else {
        todoList.forEach((item, index) => {
            console.log(`${index + 1}. ${item.text} [${item.priority}]`);
        });
    }
    console.log("\n");
}

// Add a new item with priority to the list
function addItem(itemText, priority) {
    todoList.push({ text: itemText, priority: priority });
    console.log(`Added: "${itemText}" with priority: ${priority}`);
    saveTodoList(); // Save after adding
}

// Delete an item from the list
function deleteItem(index) {
    if (index >= 0 && index < todoList.length) {
        const removedItem = todoList.splice(index, 1);
        console.log(`Deleted: "${removedItem[0].text}"`);
        saveTodoList(); // Save after deleting
    } else {
        console.log("Invalid index. Please try again.");
    }
}

// Edit an existing item
function editItem(index, newItemText, newPriority) {
    if (index >= 0 && index < todoList.length) {
        const oldItem = todoList[index];
        todoList[index] = { text: newItemText, priority: newPriority };
        console.log(`Updated: "${oldItem.text}" to "${newItemText}" with priority: ${newPriority}`);
        saveTodoList(); // Save after editing
    } else {
        console.log("Invalid index. Please try again.");
    }
}

// Display menu options
function showMenu() {
    console.log("Choose an action:");
    console.log("1. Add item");
    console.log("2. Delete item");
    console.log("3. Edit item");
    console.log("4. View to-do list");
    console.log("5. Exit");
}

// Handle user input
function handleInput(choice) {
    switch (choice) {
        case '1':
            rl.question("Enter the new item: ", (itemText) => {
                rl.question("Set priority (high, medium, low): ", (priority) => {
                    if (['high', 'medium', 'low'].includes(priority.toLowerCase())) {
                        addItem(itemText, priority.toLowerCase());
                        showMenu();
                    } else {
                        console.log("Invalid priority. Please use 'high', 'medium', or 'low'.");
                        showMenu();
                    }
                });
            });
            break;
        case '2':
            rl.question("Enter the index of the item to delete: ", (index) => {
                deleteItem(parseInt(index) - 1);
                showMenu();
            });
            break;
        case '3':
            rl.question("Enter the index of the item to edit: ", (index) => {
                const itemIndex = parseInt(index) - 1;
                if (itemIndex >= 0 && itemIndex < todoList.length) {
                    rl.question("Enter the new text for the item: ", (newItemText) => {
                        rl.question("Set new priority (high, medium, low): ", (newPriority) => {
                            if (['high', 'medium', 'low'].includes(newPriority.toLowerCase())) {
                                editItem(itemIndex, newItemText, newPriority.toLowerCase());
                                showMenu();
                            } else {
                                console.log("Invalid priority. Please use 'high', 'medium', or 'low'.");
                                showMenu();
                            }
                        });
                    });
                } else {
                    console.log("Invalid index. Please try again.");
                    showMenu();
                }
            });
            break;
        case '4':
            displayTodoList();
            showMenu();
            break;
        case '5':
            rl.close();
            console.log("Goodbye!");
            break;
        default:
            console.log("Invalid choice. Please select an option from the menu.");
            showMenu();
    }
}

// Start the app
function startApp() {
    console.log("Welcome to the To-Do List App with Priorities, Save, and Sort");
    loadTodoList(); // Load the list on startup
    showMenu();
    rl.on('line', (input) => {
        handleInput(input.trim());
    });
}

startApp();
