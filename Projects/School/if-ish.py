number1 = float(input('Pick a number, literally any number: '))
number2 = float(input('Now pick another number, literally any number: '))

if number1 == number2:
    print('Oh hey, those are the same number')
elif number1 > number2:
    print(f'Look at that, {number1} is greater than {number2}')
elif number1 < number2:
    print(f'Huh, {number1} is less than {number2}')
else:
    print('bruh')

print('')

animal = input('Hey, what is your favorite animal?\n')

if animal.lower() == 'axolotl':
    print('That is my favorite animal too!')
else:
    print('That is so cool! Not my favorite though.')