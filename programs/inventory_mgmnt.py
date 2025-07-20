inventory = {}


def add_to_inv(x, y):
    inventory[x] = y


def view():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n-----------Inventory----------------")
        for i, q in inventory.items():
            print(f"Item name: {i} --> Quantity: {q}")
        print("------------------------------------\n")


def remove_item(na):
    if na in inventory:
        x = inventory[na]
        del inventory[na]
        print(f"\nItem '{na}' with quantity {x} is removed.\n")
    else:
        print(f"\nItem '{na}' not found in inventory.\n")


while True:
    print("----------------")
    print("1. ADD ITEM")
    print("2. REMOVE ITEM")
    print("3. VIEW ITEMS")
    print("4. EXIT")
    print("----------------")

    try:
        inp = int(input("Select an option: "))
    except ValueError:
        print("Invalid input! Enter a number from 1 to 4.")
        continue

    if inp == 1:
        x = input("Item name: ")
        try:
            y = int(input("Quantity: "))
            add_to_inv(x, y)
        except ValueError:
            print("Quantity should be a number.")
    elif inp == 2:
        x = input("Item name to remove: ")
        remove_item(x)
    elif inp == 3:
        view()
    elif inp == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid input! Please select again from (1-4).")
