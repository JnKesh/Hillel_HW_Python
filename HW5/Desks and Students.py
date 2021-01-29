a = int(input("Students in Class 1: "))  # Class 1
b = int(input("Students in Class 2: "))  # Class 2
c = int(input("Students in Class 3: "))  # Class 3
print("Need to buy desks:", a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
