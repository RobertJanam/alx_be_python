def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("No item entered. Please try again.")
                
        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
            else:
                print("Current shopping list:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
                
                item_to_remove = input("Enter the item name to remove: ").strip()
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from the shopping list.")
                else:
                    print(f"'{item_to_remove}' was not found in the shopping list.")
                    
        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                print("-" * 20)
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()