from colorama import Fore
from colorama import Style

cart = []
status = 'yes'
menu = 'yes'

while menu != 'quit':
    status = 'yes'
    menu = input(f"Where you wanna go?\nGonna {Fore.GREEN}'add'{Style.RESET_ALL} anything?\nDo you want to see your {Fore.GREEN}'cart'{Style.RESET_ALL}?\nWould you rather {Fore.GREEN}'change'{Style.RESET_ALL} stuff?\nOr we can {Fore.RED}'quit'{Style.RESET_ALL} while we're ahead\nYour choice\n").lower()
    
    if menu == 'add':
        while status != 'quit':
            item = input(f"{Fore.YELLOW}What do you wanna add to your cart?\nType {Fore.RED}'quit'{Style.RESET_ALL} when you are done\n{Style.RESET_ALL}").lower()
            if item == 'quit':
                status = 'quit'
            else:
                cart.append(item)

    
    elif menu == 'cart':
        for i in range(len(cart)):
            boi = cart[i]
            print(f"{Fore.MAGENTA}{i + 1}. {boi}{Style.RESET_ALL}")

    elif menu == 'change':
        while status == 'yes':
            for i in range(len(cart)):
                boi = cart[i]
                print(f"{Fore.MAGENTA}{i + 1}. {boi}{Style.RESET_ALL}")
            indicate = int(input(f"{Fore.YELLOW}Which item would you like to change?\n{Style.RESET_ALL}"))
            new_item = input(f"{Fore.YELLOW}What is the new item?\n{Style.RESET_ALL}")
            cart[indicate - 1] = new_item
            status = input(f"Sooo...Wanna change anything else? ({Fore.GREEN}YES{Style.RESET_ALL}/{Fore.GREEN}NO{Style.RESET_ALL})\n").lower()



    else:
        if menu == 'quit':
            print(f"{Fore.CYAN}Goodbye now{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Bruh{Style.RESET_ALL}")