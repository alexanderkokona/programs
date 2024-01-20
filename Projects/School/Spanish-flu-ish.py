from colorama import Fore
from colorama import Style

with open("C:/Users/alext/Documents/Programs/Projects/School/Files/life-expectancy.csv") as file:
    # pulls out the first line in the .csv file
    header = file.readline()

    # set variables
    max_expect = -1
    max_entity = ""
    max_year = 0
    min_expect = 999999999999999
    min_entity = ""
    min_year = 0
    average = 0
    count = 0
    max_entity_int = ""
    max_expect_int = -1
    max_year_int = 0
    min_entity_int = ""
    min_expect_int = 999999999999
    min_year_int = 0
    year_int = 0

    # an input for a requested year
    year_int = input(f"{Fore.GREEN}Enter the year of interest: {Style.RESET_ALL}")

    # Organize and iterate through .csv file
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split(",")
        entity = parts[0].lower()
        year = int(parts[2])
        expect = float(parts[3])

        if expect > max_expect:
            max_expect = expect
            max_entity = entity.capitalize()
            max_year = year

        if year == year_int:
            if expect > max_expect_int:
                max_expect_int = expect
                max_entity_int = entity.capitalize()
                count += 1
                average += expect
                        
        if expect > 0 and expect < min_expect:
            min_expect = expect
            min_entity = entity.capitalize()
            min_year = year

        if year == year_int:
            if expect > 0 and expect < min_expect_int:
                min_expect_int = expect
                min_entity_int = entity.capitalize()
                count += 1
                average += expect

average = average * count

# prints all data in an organized way
# print(f"Entity: {entity} (Code: {code}), Year:{year} - Life Expectancy: {life_expect}")
    
# prints the overall greatest and least life expectancies with coresponding entity and year
print(f"The overall max life expect is: {Fore.GREEN}{max_expect}{Style.RESET_ALL} from {Fore.BLUE}{max_entity}{Style.RESET_ALL} in {Fore.YELLOW}{max_year}{Style.RESET_ALL}")
print(f"The overall min life expect is: {Fore.GREEN}{min_entity}{Style.RESET_ALL} from {Fore.BLUE}{min_entity}{Style.RESET_ALL} in {Fore.YELLOW}{min_year}{Style.RESET_ALL}")
print("")

# shows requested year
print(f"For the year {Fore.GREEN}{year_int}{Style.RESET_ALL}:")
# prints average across all countries, the greatest and least life expectancies in the requested year with the corresponding entity
print(f"The average life expect across all countries was {Fore.MAGENTA}{average:.2f}{Style.RESET_ALL}")
print(f"The max life expect was in {Fore.BLUE}{max_entity_int}{Style.RESET_ALL} with {Fore.GREEN}{max_expect_int}{Style.RESET_ALL} years")
print(f"The min life expect was in {Fore.BLUE}{min_entity_int}{Style.RESET_ALL} with {Fore.GREEN}{min_expect_int}{Style.RESET_ALL} years")
