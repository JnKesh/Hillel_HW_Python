from random import randint

m = int(input("Введите размер матрицы: "))
lst = [[randint(1, 50) for _ in range(m)] for _ in range(m)]


def sortMatrix(matrix):
    sum_colum = [0 for i in range(m)]
    for j in range(len(lst)):
        sum_colum = [sum_colum[index] + i for index, i in enumerate(lst[j])]
    print(sum_colum)

    for i in range(len(sum_colum) - 1):
        for y in range(len(sum_colum) - 1 - i):
            if sum_colum[y] >= sum_colum[y + 1]:
                sum_colum[y], sum_colum[y + 1] = sum_colum[y + 1], sum_colum[y]
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

    sum_colum = [0 for i in range(m)]
    for j in range(len(lst)):
        sum_colum = [sum_colum[index] + i for index, i in enumerate(lst[y])]

    for i in range(len(sum_colum)):
        print('{:<3}'.format(sum_colum[i]), end='   ')
    print()


lprint(lst)
z = sortMatrix(lst)
print()
lprint(lst)
