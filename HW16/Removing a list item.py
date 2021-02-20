from random import randint

a = [randint(1, 20) for _ in range(10)]
print(", ".join(str(e) for e in a))
k = int(input('Enter index: '))
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(', '.join([str(i) for i in a]))
