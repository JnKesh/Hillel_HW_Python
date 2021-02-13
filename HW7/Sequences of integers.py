a = int(input('Enter any value: '))

total = 0
quantity = 0
even = 0
odd = 0
i = []

while a != 0:
    total += a
    quantity += 1
    a = int(input('Enter any value: '))
    if quantity % 2 == 0:
        even += 1
    else:
        odd += 1
    i.append(a)

print('quantity: ', quantity)  # Количество введённых чисел
print("summary: ", total)  # Сумма всех чисел
if total == 0:
    print('average: 0')  # Среднее арифметическое при при нуле
    print('max: 0', 'min: 0')  # Максимальное и минимальное значение при нуле
else:
    print('average: ', total / quantity)  # Среднее арифметическое
    print('max: ', max(i), 'min: ', min(i))  # Максимальное и минимальное значение при
print('even: ', even)  # Четные числа
print('odd: ', odd)  # Нечетные числа
