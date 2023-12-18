n = 5
i = 0
lim = 150
flag = False
for a in range(1, lim - 3):
    if flag:
        break
    for b in range(a+1, lim):
        if flag:
            break
        for c in range(b+1, lim):
            if flag:
                break
            for d in range(c+1, lim):
                if flag:
                    break
                i += 1
                sum = a**n + b**n + c**n + d**n
                e = sum**(0.2)
                if round(e, 7) == int(e) and e < lim:
                    print(a, b, c, d, int(e), 'Сумма =', int(a + b + c + d + e))
                    print('Итерации:', i)
                    flag = True