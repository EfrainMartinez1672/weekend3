from services import add_product, show_inventory, search_product, update_product, delete_product

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
        add_product(inventory, calculate)
    elif option == "2":
        show_inventory(inventory)
    elif option == "3":
        search_product(inventory)
    elif option == "4":
        update_product(inventory)
    elif option == "5":
        delete_product(inventory)
    elif option == "6":
        print()
    elif option == "7":
        p = "r"
    else:
        print("invalid option.")