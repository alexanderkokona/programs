people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999999
youngest_name = ""

for line in people:
    parts = line.split() 
    name = parts[0]
    age = int(parts[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The youngest person is: {youngest_name} who is {youngest_age} years old")