import csv

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def overall_max_min_life_expectancy(data):
    max_row = max(data, key=lambda x: float(x['life_expectancy']))
    min_row = min(data, key=lambda x: float(x['life_expectancy']))

    print(f'The overall max life expectancy is: {max_row["Life Expectancy"]:.3f} from {max_row["Country"]} in {max_row["Year"]}')
    print(f'The overall min life expectancy is: {min_row["Life Expectancy"]:.3f} from {min_row["Country"]} in {min_row["Year"]}')

def average_max_min_life_expectancy_for_year(data, year):
    # Filter data for the specified year
    year_data = [row for row in data if row['Year'] == str(year)]

    # Average life expectancy for the specified year
    average_life_expectancy = sum(float(row['Life Expectancy']) for row in year_data) / len(year_data)

    # Max and min life expectancy for the specified year
    max_row_year = max(year_data, key=lambda x: float(x['Life Expectancy']))
    min_row_year = min(year_data, key=lambda x: float(x['Life Expectancy']))

    print(f'\nFor the year {year}:')
    print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
    print(f'The max life expectancy was in {max_row_year["Country"]} with {max_row_year["Life Expectancy"]:.3f}')
    print(f'The min life expectancy was in {min_row_year["Country"]} with {min_row_year["Life Expectancy"]:.3f}')

if __name__ == "__main__":
    # Replace 'path/to/your/life_expectancy.csv' with the actual path to your dataset file
    file_path = "C:/Users/alext/Documents/Programs/Projects/School/Files/life-expectancy.csv"
    dataset = read_csv(file_path)

    # Call the functions
    overall_max_min_life_expectancy(dataset)

    # Get user input for the year
    year_of_interest = int(input('\nEnter the year of interest: '))

    # Call the function for the specified year
    average_max_min_life_expectancy_for_year(dataset, year_of_interest)