import math

numbers = []
special_num = -1

print("Enter whole numbers until you don't feel like it anymore.\nEnter (0) to stop.")

while special_num != 0:
    special_num = float(input("Enter your number:\n"))

    if special_num != 0:
        numbers.append(special_num)
    
print()
print("===========================")

# Finds sum
sum = 0
for number in numbers:
    sum += number
print(f"The sum is {sum}")

# Finds average
average = sum / len(numbers)
print(f"The average is {average:.2f}")

# Finds greatest number
check = -1
for number in numbers:
    if number > check:
        check = number
print(f"The greatest number is {check}")

# Finds smallest number
check1 = 999999999999
for number1 in numbers:
    if number1 > 0:
        if number1 < check1:
            check1 = number1
print(f"The smallest positive number is {check1}")

# Sorts the numbers
print("===========================")
numbers.sort()
print(f"Your sorted numbers:\n{numbers}")