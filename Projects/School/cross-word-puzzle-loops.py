import random
play = 'yes'

letters = 'abcdefghijklmnopqrstuvwxyz'
capitalize = 'st'
word = "secret"
while play.lower() == 'yes':
    for row in range(len(word)):
        for col in range(len(word)):
            if row == col:
                if word[row] in capitalize:
                    print(word[row].upper(), end = ' ')
                else:
                    print(word[row], end = ' ')
            else:
                print(letters [random.randint(0, len(letters) - 1)], end = ' ')
        print()
    play = input("\nWanna go again? (YES/NO)\n").lower()