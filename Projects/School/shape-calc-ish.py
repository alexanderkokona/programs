import math
from colorama import Fore
from colorama import Style

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius * radius

boi = ""

while boi != "quit":
    boi = input(f"{Fore.MAGENTA}Hey! What boi do you have?{Style.RESET_ALL}\n")

    boi = boi.lower()

    if boi == "square":
        side = float(input("What is the length of the side?\n"))
        area = area_square(side)
        print(f"The area of the square is {Fore.GREEN}{area:.2f}{Style.RESET_ALL}")

    elif boi == "rectangle":
        length = float(input("What is the length?\n"))
        width = float(input("What is the width?\n"))
        area = area_rectangle(length, width)
        print(f"The area of the rectangle is {Fore.GREEN}{area:.2f}{Style.RESET_ALL}")

    elif boi == "circle":
        radius = float(input("What is the radius?\n"))
        area = area_circle(radius)
        print(f"The area of the circle is {Fore.GREEN}{area:.2f}{Style.RESET_ALL}")
    
    elif boi == 'quit':
        print(f"{Fore.BLUE}Goodbye now{Style.RESET_ALL}")
