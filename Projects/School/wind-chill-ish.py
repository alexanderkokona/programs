from colorama import Fore
from colorama import Style

def calculator(temp, wind_speed):
    if measure == 'C':
        temp = converter(temp)
    
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * wind_speed ** 0.16 + 0.4275 * temp * wind_speed ** 0.16

    return wind_chill

def converter(new_temp):
    new_temp = ((temp * (9/5)) + 32)
    return new_temp

temp = float(input(f"{Fore.YELLOW}What is the temperature?{Style.RESET_ALL}\n"))
measure = input(f"{Fore.YELLOW}Fahrenheit or Celsius (F/C)?{Style.RESET_ALL}\n").capitalize()

for wind_speed in range(5, 61, 5):
    wind_chill = calculator(temp, wind_speed)

    print(f"At temperature {Fore.BLUE}{temp} {measure}{Style.RESET_ALL}, and wind speed {Fore.GREEN}{wind_speed} mph{Style.RESET_ALL}, the wind chill is: {Fore.RED}{wind_chill:.2f}F{Style.RESET_ALL}")