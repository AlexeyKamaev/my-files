l =[]
for _ in range(int(input('Введите число строк для поиска:'))):
    x = input('Введите что угодно:')
    l.append(x)
l2 =[]
for _ in range(int(input('Введите кол-во тегов: '))):
    x = input('Введите тег: ').lower()
    l2.append(x)

for i in l:
    c = 0
    for k in l2:
        if k.lower() in i.lower():
            c += 1
        if c == len(l2):
            print(i)