from random import randint  # Отсылка к серверу за рандомными числами

a = [randint(1, 20) for _ in range(10)]  # Обращение к серверу за рандомными числами
print(", ".join(str(e) for e in a))  # Вывод списка с рандомными числами
k = int(input('Enter index: '))  # Индекс элемента в списке
for i in range(k + 1, len(a)):  # Сдвиг списка
    a[i - 1] = a[i]
a.pop()
print(', '.join([str(i) for i in a]))