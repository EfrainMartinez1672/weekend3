from services import add_product, show_inventory, search_product, update_product, delete_product, calculate_statistics
from archive import load_csv, save_csv

p = "e"
inventory = []
calculate = []

while p == "e":
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
        name = input("enter name product: ")
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

        quantity = input("enter product quantity: ")
        while not quantity.isdigit():
            quantity = input("enter product quantity")
        add_product(inventory, name, quantity, price)
    elif option == "2":
        show_inventory(inventory)
    elif option == "3":
        name = input("Enter product name: ")
        search_product(inventory, name)
    elif option == "4":
        name = input("Product name to update: ")

        price_input = input("New price (enter to skip): ")
        new_price = price_input if price_input != "" else None

        quantity_input = input("New quantity (enter to skip): ")
        new_quantity = quantity_input if quantity_input != "" else None
        update_product(inventory, name, new_price, new_quantity)

    elif option == "5":
        for data in inventory:
            print(f"Product: {data['name']} | quantity: {data['quantity']} | price: {data['price']}")
        name = input("which product do you want to remove?: ")
        delete_product(inventory, name)
    elif option == "6":
        calculate_statistics(inventory, calculate)
    elif option == "7":
        save_csv(inventory, "inventory.csv")
    elif option == "8":
        load_csv("inventory.csv", inventory)
    elif option == "9":
        p = "r"
    else:
        print("invalid option.")