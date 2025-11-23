def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def display_items(shopping_list):
    print("All Items")
    print("-----------")
    for idx, item in enumerate(shopping_list, start=1):
        print(f"{idx}. {item}")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (by number): ")

        if choice == '1':
            # Prompt for and add an item
            add = input("Add item: ").strip().lower()
            if add:
                shopping_list.append(add)
                print("Item added successfully.")
            else:
                print("No item added.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if shopping_list:
                display_items()
            else:
                print("Item list is empty.")
                continue
            try:
                remove = int(input("Remove item (by number): "))
                if remove:
                    if 1 <= remove <= len(shopping_list):
                        remove_index = remove - 1
                        shopping_list.pop(remove_index)
                        print("Item successfully removed.")
                    else:
                        print("Invalid number. Please enter a valid item number.")
                
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                display_items()
            else:
                print("Item list is empty.")
                continue
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    main()