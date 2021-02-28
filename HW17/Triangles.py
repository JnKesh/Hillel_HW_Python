#  треугольник a

rows = int(input("высота фигуры "))
cols = 0
for i in range(0, rows):
    cols += 1
    for j in range(0, rows - i):
        print(end="  ")
    for j in range(0, i + cols):
        if j == 0 or j == (i + cols) - 1 or i == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

#  треугольник b

rows = int(input("высота фигуры "))
cols = 0
for i in range(0, rows):
    cols += 1
    for j in range(0, rows - i):
        print(end="  ")
    for j in range(0, i + cols):
        print("*", end=" ")
    print()
print()

#  ромб c

rows = int(input('высота фигуры  '))
cols = rows * 2 - 1
i = 0
while i <= rows // 2:
    j = 0
    while j < rows * 2:
        if rows - 1 - i <= j <= rows - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1

for i in range((rows - 1) // 2):
    for j in range(cols - 1):
        if (i == j - (rows + 1) // 2
                or j == cols - i - ((rows - 1) // 2 + 2)
        ):
            print('* ', end='')
        else:
            print('  ', end='')

    print()
print()

#  ромб d

rows = int(input('высота фигуры '))
cols = rows * 2 - 1
i = 0
while i <= rows // 2:
    j = 0
    while j < rows * 2:
        if rows - 1 - i <= j <= rows - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1

for i in range((rows - 1) // 2):
    for j in range(cols - 1):
        if (i == j - (rows + 1) // 2
                or j == cols - i - ((rows - 1) // 2 + 2)
                or j == (cols - 1) // 2
        ):
            print('* ', end='')
        else:
            print('  ', end='')

    print()
print()
