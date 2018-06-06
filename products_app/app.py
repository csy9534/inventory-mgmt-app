import csv
import os

def menu(username=csy9534, products_count=100):
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset the CSV file.
    Please select an operation: """
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"REDAING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append(dict(row))

    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

def auto_incremented_id(products):
    if len(products) == 0:
        return 1
    else:
        product_ids = [int(p["id"]) for p in products]
        max_id = max(product_ids)
        next_id = max_id + 1
        return next_id

def run():
    products = read_products_from_file()

    number_of_products = len(products)
    my_menu = menu(username="@some-user", products_count=number_of_products)
    operation = input(my_menu)

    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("     " + p["id"] + " " + p["name"])

    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("What is the ID of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        new_id = auto_incremented_id(products)
        new_name = input("New product's name: ")
        new_aisle = input("New product's aisle: ")
        new_dept = input("New product's department: ")
        new_price = input("The Price: ")
        new_product = {
            "id": new_id,
            "name": new_name,
            "aisle": new_aisle,
            "department": new_dept,
            "price": new_price
        }
        products.append(new_product)
        print("CREATING A NEW PRODUCT", new_product)

    elif operation == "Update":
        product_id = input("What is the ID of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]

        update_price = input("Unpdated price: ")
        matching_product["price"] = update_price
        print("UPDATING A PRODUCT")

    elif operation == "Destroy":
        product_id = input("What is the ID of the product you want to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("DELETING A PRODUCT")

    elif operation == "Reset":
        reset_products_file()
        return
    else:
        print("Unrecognized operation. Please select one of 'List', 'Show', 'Create', 'Update', 'Destroy' or 'Reset'")

    write_products_to_file(products=products)

if __name__ == "__main__":
    run()
