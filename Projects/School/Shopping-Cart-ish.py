from colorama import Fore
from colorama import Style

print(f"{Fore.CYAN}So you wanna go to your cart? mmmmmmmm fine{Style.RESET_ALL}")
cart = []
price = []
status = 'yes'
menu = 'yes'

while menu != 'quit':
    status = 'yes'
    menu = input(f"Where you wanna go?\nGonna {Fore.GREEN}'add'{Style.RESET_ALL} anything?\nDo you want to see your {Fore.GREEN}'cart'{Style.RESET_ALL}?\nOr would you rather {Fore.GREEN}'remove'{Style.RESET_ALL} stuff?\nHow about lookin' at how much your {Fore.GREEN}'total'{Style.RESET_ALL} is?\nOr we can {Fore.RED}'quit'{Style.RESET_ALL} while we're ahead\nYour choice\n").lower()
    
    if menu == 'add':
        while status == 'yes':
            item = input(f"{Fore.YELLOW}What do you wanna add to your cart?\n{Style.RESET_ALL}").capitalize()
            cost = float(input(f"And {Fore.MAGENTA}{item}{Style.RESET_ALL} cost how much?\n"))
            cart.append(item)
            price.append(cost)
            print(f"You added {Fore.MAGENTA}{item}{Style.RESET_ALL} to the cart\n{Fore.MAGENTA}{item}{Style.RESET_ALL} costs {Fore.GREEN}${cost:.2f}{Style.RESET_ALL}\nJust so you know")
            status = input(f"Wanna keep adding stuff? ({Fore.GREEN}YES{Style.RESET_ALL}/{Fore.GREEN}NO{Style.RESET_ALL})\n").lower()
    
    elif menu == 'cart':
        for i in range(len(cart)):
            boi = cart[i]
            money = price[i]
            print(f"{Fore.MAGENTA}{i + 1}. {boi} - ${money:.2f}{Style.RESET_ALL}")

    elif menu == 'remove':
        while status == 'yes':
            for i in range(len(cart)):
                boi = cart[i]
                money = price[i]
                print(f"{Fore.MAGENTA}{i + 1}. {boi} - ${money:.2f}{Style.RESET_ALL}")
            yeet = int(input(f"{Fore.YELLOW}What item would you like to put back?{Style.RESET_ALL}\n{Fore.MAGENTA}(1-{len(cart)})\n{Style.RESET_ALL}"))
            
            while yeet < 1 or yeet >= len(cart) + 1:
                print(f"{Fore.CYAN}bruh, I need a valid option{Style.RESET_ALL}\n{Fore.RED}{yeet}{Style.RESET_ALL} is not a vaild option")
                yeet = int(input(f"{Fore.YELLOW}What item would you like to put back?{Style.RESET_ALL}\n{Fore.MAGENTA}(1-{len(cart)})\n{Style.RESET_ALL}"))

            else:
                print(f"{Fore.RED}Item removed{Style.RESET_ALL}")
                cart.pop(yeet - 1)
                price.pop(yeet - 1)
                status = input(f"Sooo...Wanna remove anything else? ({Fore.GREEN}YES{Style.RESET_ALL}/{Fore.GREEN}NO{Style.RESET_ALL})\n").lower()

    elif menu == 'total':
        total = sum(price)
        print(f"The total right now is an entire {Fore.GREEN}${total:.2f}{Style.RESET_ALL}")
        print()
        menu = input(f"Wanna go back to the {Fore.GREEN}'menu'{Style.RESET_ALL} or would you like to {Fore.RED}'quit'{Style.RESET_ALL}?\n").lower()

        if menu == 'quit':
            print(f"{Fore.CYAN}See ya{Style.RESET_ALL}")

    else:
        if menu == 'quit':
            print(f"{Fore.CYAN}Goodbye now{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Bruh{Style.RESET_ALL}")