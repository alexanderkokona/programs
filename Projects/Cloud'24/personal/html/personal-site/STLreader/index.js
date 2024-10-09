const fs = require('fs');
const stlVolume = require('stl-volume');

// Function to calculate cost based on volume and resin price
function calculateCost(volumeInCm3, pricePerMl) {
    // Convert cm^3 to ml (1 cm^3 = 1 ml)
    const volumeInMl = volumeInCm3;
    const cost = volumeInMl * pricePerMl;
    return cost.toFixed(2); // Return cost rounded to 2 decimal places
}

// Main function to handle the STL file, volume, and cost calculation
async function main(stlFilePath, pricePerMl) {
    try {
        // Read STL file
        const stlData = fs.readFileSync(stlFilePath);

        // Calculate volume in cubic centimeters (cm^3)
        const volumeInCm3 = await stlVolume(stlData);

        console.log(`Volume of the object: ${volumeInCm3.toFixed(2)} cm³`);

        // Calculate the cost
        const cost = calculateCost(volumeInCm3, pricePerMl);
        console.log(`Cost of printing: $${cost} at $${pricePerMl} per ml of resin`);
    } catch (error) {
        console.error('Error reading STL file or calculating volume:', error);
    }
}

// Example usage:
// Path to STL file and price per ml of resin
const stlFilePath = './path-to-your-file.stl';
const pricePerMl = 0.05; // Example price per ml of resin

main(stlFilePath, pricePerMl);
