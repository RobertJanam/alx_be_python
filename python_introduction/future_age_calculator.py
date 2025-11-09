# Program that takes user input and calculate their age in a future year.

current_year = 2025
future_year = 2050

difference_in_years = future_year - current_year # calculates the difference between 2025 and 2050

print("Program calculates your age in 2050 from now")
current_age = int(input("How old are you? ")) # user prompt

future_age = difference_in_years + current_age # adds your age to the current year

print(f"In 2050, you will be {future_age} years old.") # result