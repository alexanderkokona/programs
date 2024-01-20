print("Welcome to the bank of depression")

account_name = []
balance = []
status = 'yes'
menu = 'yes'

while menu != 'quit':
    status = 'yes'
    menu = input(f"Would you like to 'add' an account?\nOr 'view' your accounts?\nWould you like to see the 'totals' of your accounts?\nYou can also 'quit' but only this menu\n").lower()
    
    if menu == 'add':
        while status == 'yes':
            name = input(f"What would you like the name of this account to be?\n")
            money = float(input(f"What is the balance of this account?\n"))
            account_name.append(name)
            balance.append(money)
            status = input(f"Wanna keep adding stuff? (YES/NO)\n").lower()
    
    elif menu == 'view':
        for i in range(len(account_name)):
            boi = account_name[i]
            monies = balance[i]
            print(f"{i + 1}. {boi} - ${monies}")

    elif menu == 'totals':
        total = sum(balance)
        print(f"The total right now is an entire ${total:.2f}")
        print()
        average = total / len(balance)
        print(f"The average balance between accounts is ${average:.2f}")
        menu = input(f"Wanna go back to the 'menu' or would you like to 'quit'?\n").lower()

        if menu == 'quit':
            print(f"See ya")

    else:
        if menu == 'quit':
            print(f"Goodbye now")
        else:
            print(f"Bruh")