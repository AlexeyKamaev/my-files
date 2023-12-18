n = 5
i = 0
lim = 150
flag = False
for a in range(1, lim - 4):
    if flag:
        break
    for b in range(a+1, lim-3):
        if flag:
            break
        for c in range(b+1, lim-2):
            if flag:
                break
            for d in range(c+1, lim-1):
                if flag:
                    break
                for e in range (d+1, lim):
                    i += 1
                    if flag:
                        break
                    if a**n + b**n + c**n +d**n == e**n:
                        print(a,b,c,d,e)
                        flag = True
                        print(i)