def display_menu():
    print("\n--- Grocery List Management ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

def add_item(grocery_dict):
    item = input("Enter the name of the item to add: ")
    quantity = int(input(f"Enter the quantity of {item}: "))
    
    # If the item is already in the dictionary, add the quantity
    if item in grocery_dict:
        grocery_dict[item] += quantity
        print(f"Updated {item} quantity to {grocery_dict[item]}.")
    else:
        grocery_dict[item] = quantity
        print(f"Added {item} with quantity {quantity}.")

def remove_item(grocery_dict):
    item = input("Enter the name of the item to remove: ")
    
    if item in grocery_dict:
        quantity = int(input(f"Enter the quantity to remove for {item}: "))
        
        if quantity >= grocery_dict[item]:
            del grocery_dict[item]
            print(f"Removed {item} from the list.")
        else:
            grocery_dict[item] -= quantity
            print(f"Reduced the quantity of {item} to {grocery_dict[item]}.")
    else:
        print(f"{item} is not in the list.")

def view_items(grocery_dict):
    if grocery_dict:
        print("\n--- Current Grocery List ---")
        for item, quantity in grocery_dict.items():
            print(f"{item}: {quantity}")
    else:
        print("The grocery list is empty.")

def main():
    grocery_dict = {}
    
    while True:
        display_menu()
        choice = input("Please choose an option (1/2/3/4): ")

        if choice == '1':
            add_item(grocery_dict)
        elif choice == '2':
            remove_item(grocery_dict)
        elif choice == '3':
            view_items(grocery_dict)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "_main_":
    main()