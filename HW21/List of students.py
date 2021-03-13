src_file_name = 'src.txt'
dst_file_name = 'dst.txt'

template = '{:20}{}'
cnt = 0
tmp_sum = 0

with open(src_file_name, 'rt', encoding='utf-8') as file, \
        open(dst_file_name, 'wt', encoding='utf-8') as dst:
    for line in file:
        line = line.split()
        name = line[1] + ' ' + line[0][0] + '.'
        grades = line[2:]
        tmp_sum += sum([int(grade) for grade in grades])
        cnt += 1
        avr = round(sum([int(grade) for grade in grades]) / len(grades), 2)
        if avr < 5:
            print(template.format(name, avr))
        dst.write(template.format(name, avr))
        dst.write('\n')

print("average by class: ", round(tmp_sum / cnt, 2))
