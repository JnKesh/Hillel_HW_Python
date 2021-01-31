a = int(input("Enter 3-digit number: "))
b = a % 10  # First number
c = (a % 100) // 10  # Second number
d = (a % 1000) // 100  # Third number
print("Inverted number is:", b * 100 + c * 10 + d)
