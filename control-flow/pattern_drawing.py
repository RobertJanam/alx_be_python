number = int(input("Enter the size of the pattern: "))

limit_count = 0
while limit_count < number:
    for i in range(number):
        print("x", end="")
    limit_count += 1
    print()
    
    