// Initialize cart as an empty array
let cart = [];

// Select elements
const cartIcon = document.getElementById('cart-icon');
const cartSection = document.getElementById('cart-section');
const cartItemsContainer = document.getElementById('cart-items');
const cartTotal = document.getElementById('cart-total');
const cartCount = document.getElementById('cart-count');

// Show cart when clicking the cart icon
cartIcon.addEventListener('click', () => {
    cartSection.classList.toggle('hidden');
});

// Add to Cart function
function addToCart(productName, productPrice) {
    // Check if item is already in cart
    const existingItem = cart.find(item => item.name === productName);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            name: productName,
            price: productPrice,
            quantity: 1
        });
    }
    updateCart();
}

// Remove from Cart function
function removeFromCart(productName) {
    cart = cart.filter(item => item.name !== productName);
    updateCart();
}

// Update cart UI
function updateCart() {
    cartItemsContainer.innerHTML = ''; // Clear current items
    let total = 0;

    // Loop through cart items
    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;

        // Create cart item element
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <p>${item.name} - $${item.price.toFixed(2)} x ${item.quantity}</p>
            <button class="remove-btn" data-name="${item.name}">Remove</button>
        `;
        cartItemsContainer.appendChild(cartItem);
    });

    // Update total price and cart count
    cartTotal.innerHTML = `Total: $${total.toFixed(2)}`;
    cartCount.innerHTML = cart.length;

    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            const productName = e.target.dataset.name;
            removeFromCart(productName);
        });
    });
}

// Handle add to cart button clicks
document.querySelectorAll('.add-to-cart-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        const productItem = e.target.closest('.product-item');
        const productName = productItem.dataset.name;
        const productPrice = parseFloat(productItem.dataset.price);
        addToCart(productName, productPrice);
    });
});
