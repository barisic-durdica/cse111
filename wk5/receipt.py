# Enhancement: prints a return-by date that is 30 days in the future

import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader) # skip heading row

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    
    return dictionary

def main():
    try:
        PRODUCT_NUM_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2

        REQUEST_PROD_NUM_INDEX = 0
        REQUEST_QUANTITY_INDEX = 1

        SALES_TAX_RATE = 0.06

        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

        print("Inkom Emporium")

        total_items = 0
        subtotal = 0
        
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                prod_num = row[REQUEST_PROD_NUM_INDEX]
                quantity = int(row[REQUEST_QUANTITY_INDEX])

                product_info = products_dict[prod_num]
                product_name = product_info[PRODUCT_NAME_INDEX]
                product_price = float(product_info[PRODUCT_PRICE_INDEX])

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity
                subtotal += quantity * product_price
        
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")

        current_date_and_time = datetime.now()

        return_by = current_date_and_time + timedelta(days=30)
        print(f"Return by: {return_by.strftime("%a %b %-d %H:%M:%S %Y")}")

        print(current_date_and_time.strftime("%a %b %-d %H:%M:%S %Y"))

    except FileNotFoundError as file_not_found_err:
        print("Error: missing file")
        print(file_not_found_err)
    
    except PermissionError as perm_err:
        print("Error: permission denied")
        print(perm_err)
    
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)

if __name__ == "__main__":
    main()

