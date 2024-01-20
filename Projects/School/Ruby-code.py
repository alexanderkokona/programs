sea_green = "\033[38;5;50m"
red = "\033[0;91m"
green = "\033[0;92m"
reset = "\033[0m"

# with open("life-expectancy.csv") as file: 
    # header = file.readline() #or next(file) to skip the header line
max_expectancy = -1
max_country = ""
max_year = 0
min_expectancy = 999999999999999
min_country = ""
min_year = 0
average = 0
count = 0
max_country_intrst = ""
max_expectancy_intrst = -1
max_year_intrst = 0
min_country_intrst = ""
min_expectancy_intrst = 999999999999
min_year_intrst = 0
year_interest = 0
look = "yes"

while look == "yes":

    average = 0
    max_country_intrst = ""
    max_expectancy_intrst = -1
    max_year_intrst = 0

    min_country_intrst = ""
    min_expectancy_intrst = 999999999999
    min_year_intrst = 0
    
    look = input("Would you like to view the data? ").lower()
    if look == "yes":
        with open("life-expectancy.csv") as file: 
            header = file.readline() #or next(file) to skip the header line

            year_interest = int(input("Please enter the year of interest: "))
            for line in file:
                clean_line = line.strip()
                parts = clean_line.split(",")
                country = parts[0].lower()
                year = int(parts[2])
                expectancy = float(parts[3])


                if expectancy > max_expectancy:
                    max_expectancy = expectancy
                    max_country = country.capitalize()
                    max_year = year

                if year == year_interest:
                    if expectancy > max_expectancy_intrst:
                        max_expectancy_intrst = expectancy
                        max_country_intrst = country.capitalize()
                    count += 1
                    average += expectancy

                        
                if expectancy > 0 and expectancy < min_expectancy:
                    min_expectancy = expectancy
                    min_country = country.capitalize()
                    min_year = year

                if year == year_interest:
                    if expectancy > 0 and expectancy < min_expectancy_intrst:
                        min_expectancy_intrst = expectancy
                        min_country_intrst = country.capitalize()
                    count += 1
                    average += expectancy

        average = average / count

                
    print()
    print(f"The overall max life expectancy is:{green} {max_expectancy} for {max_country} in {max_year}{reset}.")
    print(f"The overall minimum life expectancy is {red} {min_expectancy} for {min_country} in {min_year}{reset}.")
    print()
    print(f"For the year {sea_green}{year_interest}{reset}:")
    print(f"The average life expectancy across all countries was: {sea_green}{average:.2f}{reset}")
    print(f"The max life expectancy was in {green}{max_country_intrst}{reset} with {sea_green}{max_expectancy_intrst}{reset}.")
    print(f"The minimum life expectancy was in {red}{min_country_intrst}{reset} with {sea_green}{min_expectancy_intrst}{reset}.")
    print()

print()
print(f"{sea_green}Thank you for viewing the data. Have a nice day!{reset}")