with open('funcs.txt', encoding='utf-8') as funcs:
    text = funcs.read().split('\n')
    r,t = [],[]
    for i in text:
        if 'def ' in i or '#' in i:
            r.append(i)
    if 'def' in r[0]:
        t.append(r[0])
    for i in range(len(r)-1):
        if 'def' in r[i] and 'def' in r[i+1]:
            t.append(r[i+1])

    if t == []:
        print('Best Programming Team')
    else:
        for i in t:
            print(i[i.find(' ')+1:i.find('(')])