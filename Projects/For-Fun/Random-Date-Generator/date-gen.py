import random
from colorama import Fore, Style

def else_boi():
    print(f"{Fore.MAGENTA}Date idea: {idea}{Style.RESET_ALL}")

def place_picker():
    with open("C:/Users/alext/Documents/Programs/Projects/For-Fun/Random-Date-Generator/places.csv") as file1:
        text = file1.read()
        places = list(map(str, text.split(",")))
        return random.choice(places)

def idea_generator():
    with open("C:/Users/alext/Documents/Programs/Projects/For-Fun/Random-Date-Generator/dates.csv") as file:
        allText = file.read()
        words = list(map(str, allText.split(","))) 
        return random.choice(words)
    
def baking():
    with open("C:/Users/alext/Documents/Programs/Projects/For-Fun/Random-Date-Generator/baking.csv") as file2:
        text = file2.read()
        baked = list(map(str, text.split(",")))
        return random.choice(baked)
    
def cooking():
    with open("C:/Users/alext/Documents/Programs/Projects/For-Fun/Random-Date-Generator/cooking.csv") as file3:
        text3 = file3.read()
        dish = list(map(str, text3.split(",")))
        return random.choice(dish)
    
def rand_place():
    if idea == 'road trip to random place':
        place = place_picker()
        print(f"{Fore.MAGENTA}Date idea: You should road trip to {place}{Style.RESET_ALL}")
    else:
        else_boi()

def rand_baking():
    if idea == 'bake something':
        baked = baking()
        print(f"{Fore.MAGENTA}Date idea: You should bake {baked}{Style.RESET_ALL}")
    else:
        else_boi()

def rand_cooking():
    if idea == 'cook dinner':
        cooked = cooking()
        print(f"{Fore.MAGENTA}Date idea: You should cook dinner (e.g. {cooked}){Style.RESET_ALL}")
    else:
        else_boi()

while True:
    answer = input(f"{Fore.BLUE}Are you in desperate need for a date idea? ({Style.RESET_ALL}{Fore.GREEN}yes{Style.RESET_ALL}{Fore.BLUE}/{Style.RESET_ALL}{Fore.RED}no{Style.RESET_ALL}{Fore.BLUE}){Style.RESET_ALL}\n").lower()
    
    if answer == 'yes':
        idea = idea_generator()

        # for random place option
        

        # for the baking option
        

        # for the cooking option
        

        # normal response 
        

        # ask to run program again
        another_idea = input(f"{Fore.BLUE}Would you like another date idea?{Style.RESET_ALL}\n").lower()
        if another_idea != 'yes':
            break

    elif answer == 'no':
        print(f"{Fore.BLUE}Goodbye and good luck{Style.RESET_ALL}")
        break

    else:
        print(f"{Fore.RED}Please enter a valid response (yes/no){Style.RESET_ALL}")
