while True:
    s = list(map(int, input('Enter pupils heights: ').split()))
    if max(s) > 200:  # Проверка списка на максимальное значение
        print('Only numbers between 1 and 200 are accepted, try again.')
    if min(s) < 1:
        print('Only numbers between 1 and 200 are accepted, try again.')
    else:
        break
while True:
    r = int(input("Enter Peter's height: "))
    if not 1 <= r <= 200:  # Проверка числа на максимальное значение
        print('Only numbers between 1 and 200 are accepted, try again')
    else:
        break
count = 0
for i in range(len(s)):
    if r <= s[i]:
        count += 1
print(count + 1)
