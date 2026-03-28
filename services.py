
def add_product(inventory, name, quantity, price):

    quantity = int(quantity)

    products = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(products)
    
def show_inventory(inventory):
    if inventory: 
        for data in inventory:
            print(f"product: {data["name"]} | price {data["price"]} | quantity {data["quantity"]}")

def search_product(inventory, name):
    for data in inventory:
        if name.lower() == data["name"]:
            print(f"Product found: {name}")
            return
        
    print("Product dont found")

def update_product(inventory, name, new_price=None, new_quantity=None):
    p = "e"
    c = "e"

    for data in inventory:
        if data["name"].lower() == name.lower():

            while p == "e":
                if new_price is None:
                    p = "r"
                else:
                    try:
                        new_price = float(new_price)
                        if new_price < 0:
                            print("Invalid price.")
                            return
                        else:
                            p = "r"
                    except ValueError:
                        print("Invalid price.")
                        return

            while c == "e":
                if new_quantity is None:
                    c = "r"
                else:
                    try:
                        new_quantity = int(new_quantity)
                        if new_quantity < 0:
                            print("Invalid quantity.")
                            return
                        else:
                            data["price"] = new_price if new_price is not None else data["price"]
                            data["quantity"] = new_quantity
                            print("Product updated successfully")
                            c = "r"
                    except ValueError:
                        print("Invalid quantity.")
                        return
            return

    print("Product not found.")

def delete_product(inventory, name):

    for  data in inventory:
        if data["name"].lower() == name:
            inventory.remove(data)
            print("product deleted.")
            return
    print("product not found.")

def calculate_statistics(inventory, calculate):
    for data in inventory:
        price_cl = data.get("price")
        quantity_cl = data.get("quantity")
        
        calculate.append(price_cl * quantity_cl)
    print(f"total is: {sum(calculate)}")
    calculate.clear()    