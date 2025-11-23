def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (by number): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print("Item added successfully.")
            else:
                print("No item added.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Item list is empty.")
            else:
                # Display items with numbers
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                
                try:
                    remove_choice = int(input("Remove item (by number): "))
                    if 1 <= remove_choice <= len(shopping_list):
                        removed_item = shopping_list.pop(remove_choice - 1)
                        print("Item successfully removed.")
                    else:
                        print("Invalid number. Please enter a valid item number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Item list is empty.")
            else:
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()