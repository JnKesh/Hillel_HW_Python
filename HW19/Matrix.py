from random import randint

m = int(input("Enter size of matrix: "))
lst = [[randint(1, 50) for _ in range(m)] for _ in range(m)]


def sortMatrix(matrix):
    sum_column = [0 for i in range(m)]
    for j in range(len(lst)):
        sum_column = [sum_column[index] + i for index, i in enumerate(lst[j])]
    print(sum_column)

    for i in range(len(sum_column) - 1):
        for y in range(len(sum_column) - 1 - i):
            if sum_column[y] >= sum_column[y + 1]:
                sum_column[y], sum_column[y + 1] = sum_column[y + 1], sum_column[y]
                for j in range(len(lst)):
                    matrix[j][y], matrix[j][y + 1] = matrix[j][y + 1], matrix[j][y]

    for x in range(len(lst)):
        for i in range(len(lst) - 1):
            for y in range(len(lst) - i - 1):
                if x % 2 != 0:
                    if matrix[y][x] > matrix[y + 1][x]:
                        matrix[y][x], matrix[y + 1][x] = matrix[y + 1][x], matrix[y][x]
                else:
                    if matrix[y][x] < matrix[y + 1][x]:
                        matrix[y][x], matrix[y + 1][x] = matrix[y + 1][x], matrix[y][x]

    return matrix


def lprint(matrix1):
    for i in range(len(lst)):
        for y in range(len(lst[i])):
            print('{:<3}'.format(lst[i][y]), end='   ')
        print()

    sum_column = [0 for i in range(m)]
    for j in range(len(lst)):
        sum_column = [sum_column[index] + i for index, i in enumerate(lst[y])]

    for i in range(len(sum_column)):
        print('{:<3}'.format(sum_column[i]), end='   ')
    print()


lprint(lst)
z = sortMatrix(lst)
print()
lprint(lst)
