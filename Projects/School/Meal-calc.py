print('Welcome to The Kokona Coconut Grill!')
child_meal = float(input('What is the price of a child meal? '))
children = int(input('And how many children are there? '))
adult_meal = float(input('What is the price of an adult meal? '))
adults = int(input('And how many adults are there? '))
drink_price = float(input('What is the price for a kid drink? '))
drink_number = int(input('How many kid drinks are you getting? '))
drink_price2 = float(input('What is the price for a regular drink? '))
drink_number2 = int(input('How many regular drinks are you getting? '))
birthday = int(input('How many birthdays do we have today? '))
sales_tax_rate = float(input('What is the sales tax rate? '))

subtotal = ((child_meal * children) + (adult_meal * adults) + (drink_price * drink_number) + (drink_price2 * drink_number2) - birthday * child_meal )
sales_tax = (subtotal * sales_tax_rate) / 100
total = subtotal + sales_tax

print('')
print(f'Your subtotal is: ${subtotal:.2f}')
print(f'The sales tax is ${sales_tax:.2f}')
print(f'Your total is: ${total:.2f}')

print('')
payment = float(input('What is the payment amount? '))
change = payment - total
str(change)
print(f'Your change is ${change:.2f}')
print('Thank you for coming! Hope to see you again!')