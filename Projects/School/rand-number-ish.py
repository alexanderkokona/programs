import random

again = "yes"

while again == "yes":
    number = random.randint(1, 100)

    guess_counter = 0

    guess = -1

    while guess != number:
        guess = int(input("What be your guess?\n"))
        guess_counter = guess_counter + 1

        if guess < number:
            print("mmmmmm\nHigher")
        elif guess > number:
            print("uuuuuuuu\nLower")
        else:
            print("You done did got it!")

    print(f"It only took {guess_counter} guesses")

    again = input("Wanna go again? (yes/no)\n").lower()

print("Tanks for playing. Bye now.")