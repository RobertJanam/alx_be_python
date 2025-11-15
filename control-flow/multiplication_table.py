# print multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 10):
    ans = number * y # calculation
    print("{} * {} = {}".format(number, y, ans)) # output