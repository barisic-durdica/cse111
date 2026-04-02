import csv

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
    PRODUCT_NUM_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

    REQUEST_PROD_NUM_INDEX = 0
    REQUEST_QUANTITY_INDEX = 1

    products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

    print("All Products")
    print(products_dict)

    print("Requested Items")
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row in reader:
            prod_num = row[REQUEST_PROD_NUM_INDEX]
            quantity = row[REQUEST_QUANTITY_INDEX]

            product_info = products_dict[prod_num]
            product_name = product_info[PRODUCT_NAME_INDEX]
            product_price = product_info[PRODUCT_PRICE_INDEX]

            print(f"{product_name}: {quantity} @ {product_price}")

if __name__ == "__main__":
    main()

