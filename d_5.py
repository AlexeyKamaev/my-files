a, b, c = 1, 2, 3
lim = 10**10
n = 5
nd = 1/n
i = 0
flag = False

for d in range(c + 1, lim - 1):
    if flag:
        break
    i = + 1

    sum5 = a ** n + b ** n + c ** n + d ** n
    e = sum5 ** (0.1)

    if round(e,20) == int(e):
        e = int(e)
        print(a, b, c, d, e)
        flag = True
        print('Всего:', i)
else:
    print('Всего:', i,'\nd & e не найдены')