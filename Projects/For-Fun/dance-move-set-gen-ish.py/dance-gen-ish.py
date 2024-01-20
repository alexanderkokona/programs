import random
from colorama import Fore, Style

def move_gen():
    with open(r"C:\Users\alext\Documents\Programs\Projects\For-Fun\dance-move-set-gen-ish.py\moves.csv") as file:
        allText = file.read()
        moves = list(map(str, allText.split(",")))
        length = random.randint(1, len(moves))  # Generate a random length for the move set
        return ', '.join(random.choices(moves, k=length))  # Randomly select moves based on the generated length

while True:
    answer = input(f"{Fore.BLUE}Are you in desperate need for a move set? ({Style.RESET_ALL}{Fore.GREEN}yes{Style.RESET_ALL}{Fore.BLUE}/{Style.RESET_ALL}{Fore.RED}no{Style.RESET_ALL}{Fore.BLUE}){Style.RESET_ALL}\n").lower()
    
    if answer == 'yes':
        idea = move_gen()
        print(f"{Fore.MAGENTA}Move set: {idea}{Style.RESET_ALL}")
        
    else:
        print(f"{Fore.RED}Please enter a valid response (yes/no){Style.RESET_ALL}")
        continue
    
    another_idea = input(f"{Fore.BLUE}Would you like another move set?{Style.RESET_ALL}\n").lower()
    
    if another_idea != 'yes':
        print(f"{Fore.BLUE}Goodbye and good luck{Style.RESET_ALL}")
        break
