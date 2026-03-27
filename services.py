
def add_product(inventory, calculate):
    name = input("enter name product: ")
    p = "e"
    while p == "e":
        try:
            price = float(input("enter product price: "))
            if price < 0:
                print("just put positive numbers.")
            else:
                p = "r"
        except ValueError:
            print("enter only integers.")

    quantity = input("enter product quantity: ")
    while not quantity.isdigit():
        quantity = input("enter product quantity")

    quantity = int(quantity)

    products = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(products)
    calculate.append(price * quantity)
    
def show_inventory(inventory):
    if inventory: 
        for data in inventory:
            print(f"product: {data["name"]} | price {data["price"]} | quantity {data["quantity"]}")

def search_product(inventory):
    name = input("enter product name: ")
    for data in inventory:
        if name.lower() == data["name"]:
            print(f"Product found: {name}")
        else:
            print("Product dont found")

def update_product(inventory, calculate):
    p = "e"
    c = "e"
    print("Which product do you want to modify?")

    for data in inventory:
        print(f"Product: {data['name']} | quantity: {data['quantity']} | price: {data['price']}")

    name = input("Enter product name: ").lower()

    for data in inventory:
        if data["name"].lower() == name:
            while p == "e":
                try:
                    new_price = float(input("Enter new price: "))
                    if new_price < 0:
                        print("Invalid price.")
                        continue
                    else:
                        p = "r"
                except ValueError:
                    print("Invalid")
                    continue
            while c == "e":
                try:
                    new_quantity = int(input("Enter quantity: "))
                    if new_quantity < 0:
                        print("Invalid quantity.")
                        continue
                    else:
                        c = "r"
                    data["price"] = new_price
                    data["quantity"] = new_quantity
                    print("Product updated successfully")
                    
                    calculate.append(new_price * new_quantity)
                    return
                except ValueError:
                    print("Invalid")
                    continue

    print("Product not found.")

def delete_product(inventory):

    for data in inventory:
        print(f"Product: {data['name']} | quantity: {data['quantity']} | price: {data['price']}")
    product = input("which product do you want to remove?: ")
    for  data in inventory:
        if data["name"].lower() == product:
            inventory.remove(data)
            print("product deleted.")
        else:
            print("product not found.")

def calculate_statistics():
    