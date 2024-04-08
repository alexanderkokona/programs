import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    """
    compound_dict = {}
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict

def main():
    try:
        # Call read_dictionary function to read products.csv
        products_dict = read_dictionary("products.csv", 0)

        # Print the store name
        print("Store: XYZ Mart")
        print("Receipt")
        print("-" * 30)

        total_items = 0
        subtotal = 0

        # Open request.csv file for reading
        with open("request.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                # Check if the product exists in products_dict
                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])

                    # Print product name, requested quantity, and product price
                    print(f"Product: {product_name}, Quantity: {quantity}, Price: {product_price}")
                    
                    # Update total items and subtotal
                    total_items += quantity
                    subtotal += quantity * product_price
                else:
                    print(f"Product with number {product_number} not found.")

        # Print total number of items
        print(f"Total Items: {total_items}")

        # Print subtotal
        print(f"Subtotal: ${subtotal:.2f}")

        # Compute and print sales tax
        sales_tax_rate = 0.06
        sales_tax_amount = subtotal * sales_tax_rate
        print(f"Sales Tax (6%): ${sales_tax_amount:.2f}")

        # Compute and print total amount due
        total_amount_due = subtotal + sales_tax_amount
        print(f"Total Amount Due: ${total_amount_due:.2f}")

        # Print thank you message
        print("Thank you for shopping with us!")

        # Print current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Date and Time: ", current_datetime)

    except FileNotFoundError:
        print("Error: File not found.")
    except KeyError:
        print("Error: KeyError occurred. Please check the data files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure to close any open file handles
        file.close()

if __name__ == "__main__":
    main()
