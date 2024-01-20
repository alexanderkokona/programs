word = 'Jehovah'

fav_letter = input("Tell me, what's your favorite letter?\n")

for letter in word:
    if letter.lower() == fav_letter.lower():
        print(letter.upper(), end = '')
    else:
        print(letter.lower(), end = '')
print()

for letter in word:
    if letter.lower() == fav_letter.lower():
        print('_', end = '')
    else:
        print(letter.lower(), end = '')
print()