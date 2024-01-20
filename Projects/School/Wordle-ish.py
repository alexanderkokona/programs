import random

def setup():
    jesus_names = ["Jesus", "Jehovah", "One", "God", "Christ", "Yeshuah", "Joseph", "Yawe", "Holy", "Word", "Wonderful", "Counselor", "Peace", "Light"]
    mt_dew = ["Original", "Red", "Voodoo", "Midnight", "Voltage"]
    language = ["Python", "Ruby", "C#", "C++", "Rust", "Java"]
    print("Oh hey, so you wanna play a game?")
    theme = int(input("What would you like the theme for this game to be?\nYour options are:\n1. Jesus\n2. Mt. Dew\n3. Programming Languages\n"))
    if theme == 1:
        return jesus_names
    elif theme == 2:
        return mt_dew
    elif theme == 3:
        return language
    else:
        print("bruh")
        return setup()

def display(spaces):
    new_space = ""
    for i in spaces:
        new_space += i
        new_space += (" ")
    hint = (f"Here's a hint: {new_space}")
    print(hint)
    

def game():
    theme = setup()
    answer = random.choice(theme).lower()
    answer_len = len(answer)
    spaces = ""
    for i in range(answer_len):
        spaces += "_"
    hint = (f"Here's a hint: {spaces}")
    guesses = 1

    display(spaces)
    guess = input("Question: What is the answer?\n").lower()

    while guess != answer:
        if len(guess) > answer_len or len(guess) < answer_len:
            print("Sorry, but that's not the right amount of characters")
            display(spaces)
            guess = input("Question: What is the answer?\n").lower()

        else:
            new_hint = list(spaces)
            for position in range(answer_len):
                if answer[position] == guess[position]:
                    new_hint[position] = guess[position].upper()
                elif guess[position] in answer:
                    new_hint[position] = guess[position]
            
            guesses += 1
            spaces = new_hint
            display(spaces)
            guess = input("What is the answer?\n").lower()

    print (f"You got it! The word was {answer.capitalize()}!")
    print(f"It took {guesses} tries!")
    again = input("Wanna play again? (YES/NO)\n").lower()
    if again == 'yes':
        restart(answer)

# Call restart function when answer is right to reset values
def restart(answer):
    game()

game()

print("Oh, okay then...")