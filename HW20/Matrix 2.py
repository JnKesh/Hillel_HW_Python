from random import randint

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

lst_column = [[randint(1, 50) for lst in range(c)] for lst2 in range(r)]
total_sum = 0

for lst2 in range(r):
    for lst in range(c):
        total_sum += lst_column[lst2][lst]
        print("{:<3}".format(lst_column[lst2][lst]), end="  ")
    print("    ", total_sum)
    total_sum = 0
print()

total_sum1 = [0 for lst in range(c)]
for y in range(len(lst_column)):
    total_sum1 = [total_sum1[index] + lst for index, lst in enumerate(lst_column[y])]

for lst in range(len(total_sum1)):
    print("{:<3}".format(total_sum1[lst]), end="  ")
