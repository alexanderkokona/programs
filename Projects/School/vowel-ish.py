vowels = 'aeiou'
word = input("What would you like?\n")
article = 'a'
if word[0] in vowels:
    article = 'an'

print(f"You want {article} {word}")