from flags_script import *

x = int(input('Введите номер поля:'))
names = tuple(range(37))
names2 = list()
X = 1  # 1 и 3 секция, черные четные
flags_maker()

for i in names:

    if i == 0:
        names2.append(0)
    if (X == 1 and i % 2 == 0) or (X == -1 and i % 2 != 0):
        names2.append(1)
    else:
        names2.append(2)
    if i in flags:
        X = -X

if x in names:
    if names2[x] == 0:
        print('зеленый')
    elif names2[x] == 1:
        print('красный')
    elif names2[x] == 2:
        print('черный')
else:
    print('ошибка ввода')