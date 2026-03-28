def add_product(inventory, name, quantity, price):
    # convert quantity to int
    quantity = int(quantity)

    # create a product dictionary
    products = {
        "name": name,      # product name
        "price": price,    # product price
        "quantity": quantity  # product quantity
    }
    # add product to inventory list
    inventory.append(products)
    
def show_inventory(inventory):
    # check if inventory is not empty
    if inventory: 
        for data in inventory:
            # print product info
            print(f"product: {data['name']} | price {data['price']} | quantity {data['quantity']}")

def search_product(inventory, name):
    # search for product by name
    for data in inventory:
        if name.lower() == data["name"].lower():  # ignore case
            print(f"Product found: {name}")
            return
        
    # print if product not found
    print("Product not found")

def update_product(inventory, name, new_price=None, new_quantity=None):
    # flags for checking input
    p = "e"
    c = "e"

    for data in inventory:
        if data["name"].lower() == name.lower():  # ignore case

            # update price
            while p == "e":
                if new_price is None:
                    p = "r"
                else:
                    try:
                        new_price = float(new_price)  # convert to float
                        if new_price < 0:
                            print("Invalid price.")
                            return
                        else:
                            p = "r"
                    except ValueError:
                        print("Invalid price.")
                        return

            # update quantity
            while c == "e":
                if new_quantity is None:
                    c = "r"
                else:
                    try:
                        new_quantity = int(new_quantity)  # convert to int
                        if new_quantity < 0:
                            print("Invalid quantity.")
                            return
                        else:
                            # update product info
                            data["price"] = new_price if new_price is not None else data["price"]
                            data["quantity"] = new_quantity
                            print("Product updated successfully")
                            c = "r"
                    except ValueError:
                        print("Invalid quantity.")
                        return
            return

    # print if product not found
    print("Product not found.")

def delete_product(inventory, name):
    # search product to delete
    for data in inventory:
        if data["name"].lower() == name.lower():  # ignore case
            inventory.remove(data)  # remove from inventory
            print("product deleted.")
            return
    # print if not found
    print("product not found.")

def calculate_statistics(inventory, calculate):
    # calculate total value
    for data in inventory:
        price_cl = data.get("price")       # get price
        quantity_cl = data.get("quantity") # get quantity
        calculate.append(price_cl * quantity_cl)  # add to list
    # print total
    print(f"total is: {sum(calculate)}")
    calculate.clear()  # clear list for next time