import math
from datetime import date

def calculate_tire_volume(w, a, d):
    # Constants
    pi = math.pi
    conversion_factor = 10000000000
    
    # Calculate the volume using the provided equation
    volume = (pi * w**2 * a * (w * a + 2540 * d)) / conversion_factor
    
    return volume

# Get input from the user
width = float(input("Enter the width of the tire (in mm): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire (in inches): "))

# Calculate the volume
tire_volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Get the current date
current_date = date.today()

# Display the result
print("The volume of the tire is:", tire_volume, "liters")

# Append to volumes.txt file
with open('volumes.txt', 'a') as file:
    file.write(f"{current_date}\t{width}\t{aspect_ratio}\t{diameter}\t{tire_volume}\n")

print("Data appended to volumes.txt")
