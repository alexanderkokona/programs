friends = []

names = input("What is the name of a friend: ")

while names != 'end':
    if names == 'end':
        break
    else:
        friends.append(names)
        names = input("What is the name of a friend: ")

print("Your frineds are:")
for name in friends:
    print(name, end = " ")