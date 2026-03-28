from services import add_product, show_inventory, search_product, update_product, delete_product, calculate_statistics
from archive import load_csv, save_csv

p = "e"
inventory = []   # list to store products
calculate = []   # list to store temporary calculation

while p == "e":
    # print menu
    print("\n1.add")
    print("2.show")
    print("3.search")
    print("4.update")
    print("5.delete")
    print("6.Statistics")
    print("7.Save CSV")
    print("8.Upload CSV")
    print("9.exit")
    option = input("Which option do you wish to perform?: ")

    if option == "1":
        # get product name
        name = input("enter name product: ")

        # get product price
        t = "e"
        while t == "e":
            try:
                price = float(input("enter product price: "))
                if price < 0:
                    print("just put positive numbers.")
                else:
                    t = "r"
            except ValueError:
                print("enter only integers.")

        # get product quantity
        quantity = input("enter product quantity: ")
        while not quantity.isdigit():
            quantity = input("enter product quantity")
        
        # add product to inventory
        add_product(inventory, name, quantity, price)

    elif option == "2":
        # show all products
        show_inventory(inventory)

    elif option == "3":
        # search for a product by name
        name = input("Enter product name: ")
        search_product(inventory, name)

    elif option == "4":
        # update product info
        name = input("Product name to update: ")

        price_input = input("New price (enter to skip): ")
        new_price = price_input if price_input != "" else None

        quantity_input = input("New quantity (enter to skip): ")
        new_quantity = quantity_input if quantity_input != "" else None

        # update product in inventory
        update_product(inventory, name, new_price, new_quantity)

    elif option == "5":
        # show products before deleting
        for data in inventory:
            print(f"Product: {data['name']} | quantity: {data['quantity']} | price: {data['price']}")
        
        # get product name to remove
        name = input("which product do you want to remove?: ")
        delete_product(inventory, name)

    elif option == "6":
        # calculate total inventory value
        calculate_statistics(inventory, calculate)

    elif option == "7":
        # save inventory to CSV
        save_csv(inventory, "inventory.csv")

    elif option == "8":
        # load inventory from CSV
        load_csv("inventory.csv", inventory)

    elif option == "9":
        # exit program
        p = "r"

    else:
        # invalid menu option
        print("invalid option.")