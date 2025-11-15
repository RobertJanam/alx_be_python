task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a high priority task but isn't time sensitive. Consider completing it when you have free time.")
        else:
            print("Invalid input. Please enter (yes/no).")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task but requires immediate attention due to time sensitivity.")
        elif time_bound == "no":
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input. Please enter (yes/no).")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but requires immediate attention due to time sensitivity.")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input. Please enter (yes/no).")
    
    case _:
        print("Invalid choice. Please enter one of this options (low/medium/high).")