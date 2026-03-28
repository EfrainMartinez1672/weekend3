import csv

# Guardar inventario en CSV
def save_csv(inventory, path):
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        return

    try:
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Escribir encabezado
            writer.writerow(["name", "price", "quantity"])

            # Escribir productos
            for product in inventory:
                writer.writerow([product["name"], product["price"], product["quantity"]])

        print(f"Inventory saved in: {path}")

    except:
        print("Error: cannot save the file.")


# Cargar inventario desde CSV
def load_csv(path, inventory):
    try:
        with open(path, mode="r") as file:
            reader = csv.reader(file)

            # Leer encabezado
            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print("Error: wrong header.")
                return

            loaded = []
            for row in reader:
                if len(row) != 3:
                    continue  # fila inválida
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])
                if price < 0 or quantity < 0:
                    continue
                loaded.append({"name": name, "price": price, "quantity": quantity})

        # Preguntar al usuario
        option = input("Overwrite inventory? (Y/N): ").upper()
        if option == "Y":
            inventory.clear()
            inventory.extend(loaded)
            print("Inventory replaced.")
        else:
            # Fusionar: sumar cantidades y actualizar precio
            for new in loaded:
                found = False
                for old in inventory:
                    if old["name"].lower() == new["name"].lower():
                        old["quantity"] += new["quantity"]
                        old["price"] = new["price"]
                        found = True
                        break
                if not found:
                    inventory.append(new)
            print("Inventory merged.")

    except:
        print("Error: cannot load the file.")