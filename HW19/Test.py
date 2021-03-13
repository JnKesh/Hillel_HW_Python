from random import randint

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
a = []

lst = [[randint(1, 10) for i in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        print(lst[i][j], end=' ')
    print()

for i in range(m):
    print(" --", end='')
print()

for i in range(m):
    s = 0
    for j in range(n):
        s += a[i][j]
    print("%3d" % s, end='')
print()

# sum rows
sum_row = [0] * len(lst)
for i, row in enumerate(lst):
    for item in row:
        sum_row[i] += item

# sum columns
sum_col = [0] * len(lst[0])
for row in lst:
    for i, item in enumerate(row):
        sum_col[i] += item
