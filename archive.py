import csv

def save_csv(inventory, path):
    # check if inventory is empty
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        return

    try:
        # open file to write
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # write header
            writer.writerow(["name", "price", "quantity"])

            # write each product
            for product in inventory:
                writer.writerow([product["name"], product["price"], product["quantity"]])

        print(f"Inventory saved in: {path}")

    except:
        # error if cannot save
        print("Error: cannot save the file.")


def load_csv(path, inventory):
    try:
        # open file to read
        with open(path, mode="r") as file:
            reader = csv.reader(file)

            # read header and check
            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print("Error: wrong header.")
                return

            loaded = []
            # read rows
            for row in reader:
                if len(row) != 3:
                    continue  # invalid row
                name = row[0]
                price = float(row[1])       # convert price to float
                quantity = int(row[2])      # convert quantity to int
                if price < 0 or quantity < 0:
                    continue
                loaded.append({"name": name, "price": price, "quantity": quantity})

        # ask user to overwrite or merge
        option = input("Overwrite inventory? (Y/N): ").upper()
        if option == "Y":
            inventory.clear()           # remove old inventory
            inventory.extend(loaded)    # add loaded inventory
            print("Inventory replaced.")
        else:
            # merge loaded inventory with existing
            for new in loaded:
                found = False
                for old in inventory:
                    if old["name"].lower() == new["name"].lower():
                        old["quantity"] += new["quantity"]  # add quantity
                        old["price"] = new["price"]        # update price
                        found = True
                        break
                if not found:
                    inventory.append(new)  # add new product
            print("Inventory merged.")

    except:
        # error if cannot load
        print("Error: cannot load the file.")