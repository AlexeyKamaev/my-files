n = int(input())
numbers = [i for i in range(1, n ** 2 + 1)]
m = [[int(i) for i in input().split()] for _ in range(n)]
mc = [sum(i) for i in m]
m1 = []
m2,m3 = [],[]
cols,cc,sumM,sumS = 0,0,0,0
flag = True
for i in m:
    m1.extend(i)
for i in m1:  # разные числа от 1 до n**2
    if m1.count(i) != 1:
        flag = False
    if i not in numbers:
        flag = False

for i in range(n): # разворачиваем матрицу
    for j in range(n):
        if i == j:
            sumM += m[i][j]
        if i+j == n-1 :
            sumS += m[i][j]
        m2.append(m[n-1-j][i])
for i in m2:
    if cc == n:
        m3.append(cols)
        cols = i
        cc = 1
    else:
        cols += int(i)
        cc += 1
m3.append(cols)

if m3.count(mc[0]) != len(mc) or mc.count(mc[0]) != len(mc) or sumM != sumS or sumM != mc[0]:
    flag = False

print('YES' if flag == True else 'NO')