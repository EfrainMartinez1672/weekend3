historial = []
def add_product(inventory, name, price, quantity):
    inventory = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    historial.append(inventory)