s = str(input('Enter text here: '))
ch = str(input('Enter character to find here: '))
start = -1
while True:
    start = s.find(ch, start + 1)
    if start == -1:
        break
    print('Matches found at the index:', start)
