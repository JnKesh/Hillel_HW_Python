from random import randint

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
a = []

lst = [[randint(1, 50) for _ in range(m)] for _ in range(n)]

# sum rows
sum_m = [0] * len(lst)
for i, row in enumerate(lst):
    for item in row:
        sum_m[i] += item

# sum columns
sum_n = [0] * len(lst[0])
for row in lst:
    for i, item in enumerate(row):
        sum_n[i] += item

print(sum_m)
print()
print(sum_n)
