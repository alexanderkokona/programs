# # even worse
# # list = ['one']

# # Gross / smells
# movies = list()

# movies.append("Dune")
# movies.append("Mission Impossible")

# # eww
# print(movies)

# #wayyyyy better
# movie = [
#     "Batman Begins",
#     "Reign of Fire",
#     "Star Wars"
# ]

# # User friendly print sequence
# print('\nMovies:')
# for movie in movies:
#     print(f'- {movie}')

# # takes the fourth boi out to use 
# movie3 = movies[3]
# # prints fourth movie, cause 0 and ish
# print(movies[3])
# # prints 'r' 
# print('Word'[2])


# Ordering App

# memory to store inputs
cart = []
print()
# the menu that is looped
menu = [
    '1 - Drink',
    '2 - Entree',
    '3 - Side',
    '4 - Dessert',
]

drinks = ["Water", "Root Beer", "Guarana", "Smoothie"]

#showcasing append again
menu.append('5 - Done ordering')

selection = 0
while selection != 5:
    print('What would you like to order?\n')
    for item in menu:
        print(item)
    selection = int(input('Enter 1 - 5\n'))
    # checks for valid option
    if selection < 1 or selection > 5:
        print(f'You entered {selection} which is not a valid option, please try again.')
    # goes into the drink list
    elif selection == 1:
        print("What drink would you like to order")
        for drink in drinks:
            print(drink)
        drink_selection = input("Drink choice:\n").capitalize()
        cart.append(drink_selection)
    # ensures invalid options are not appended
    elif selection != 5:
        cart.append(selection)

# prints your list that was stored in cart
print("You selected:")
for item in cart:
    print(f'-{item}')