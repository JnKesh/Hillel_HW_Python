s = str(input('Enter text here: '))
ch = str(input('Enter character to find here: '))
start = 0

while ch in s:
    start = s.find(ch, start+1)  # Поиска символа
    for i in range(len(s)):  # Его индекс
        if s[i] == ch:
            index = i
            print('Matches found at the index:', index)
    break
else:
    print('No matches found')
print('Searching complete.')
