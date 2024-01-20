print("What's good, nerd?")
grade = float(input("Tell me, what's your grade percentage in any class\n"))

# Tree for A
if grade >= 90:
    letter = ("Oh, that's an A. Well done.")

# Tree for B
elif grade >= 80 and grade < 90:
    letter = ("Huh, a B. Nice work.")

# Tree for C
elif grade >= 70 and grade < 80:
    letter = ("That's a C. But you know the saying, 'C's get degress.")

# Tree for D
elif grade >= 60 and grade < 70:
    letter = ("Oh tough, that's a D.")

# Tree for F
elif grade < 60:
    letter = ("Yikes, that's an F. Better get a tutor or somethin' 'cause that's no good.")

# Just in case
else: 
    print("Bruh, a vaild number would be nice.")

# print letter
print(letter)

# Pass or fail
if grade >= 70:
    print("That's a passing grade!")
else:
    print("Yeah, that's not a passing grade...")

