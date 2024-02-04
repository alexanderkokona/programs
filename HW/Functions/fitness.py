from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Function to convert pounds to kilograms
def pounds_to_kg(weight_pounds):
    return weight_pounds * 0.45359237

# Function to convert inches to centimeters
def inches_to_cm(height_inches):
    return height_inches * 2.54

# Function to calculate BMI
def calculate_bmi(weight_kg, height_cm):
    return weight_kg / ((height_cm / 100) ** 2)

# Function to calculate BMR (using Harris-Benedict equation for adults)
def calculate_bmr(gender, weight_kg, height_cm, age):
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        return None

# Get user input
gender = input("Enter your gender: ")
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
weight_pounds = float(input("Enter your weight in U.S. pounds: "))
height_inches = float(input("Enter your height in U.S. inches: "))

# Calculate age, convert units, and calculate BMI and BMR
age = calculate_age(birthdate)
weight_kg = pounds_to_kg(weight_pounds)
height_cm = inches_to_cm(height_inches)
bmi = calculate_bmi(weight_kg, height_cm)
bmr = calculate_bmr(gender, weight_kg, height_cm, age)

# Print the results
print(f"\nAge: {age} years")
print(f"Weight: {weight_kg:.2f} kg")
print(f"Height: {height_cm:.2f} cm")
print(f"BMI: {bmi:.2f}")
print(f"BMR: {bmr:.2f} calories/day")
