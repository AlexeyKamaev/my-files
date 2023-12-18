a1, b1, a2, b2 = int(input()),int(input()),int(input()),int(input())
list_1 = list(range(a1, b1+1))
list_2 = list(range(a2, b2+1))
list_3 = []

for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(i)
            break

if len(list_3) == 0:
    print ('пустое множество')
else:
    if list_3[0] == list_3[len(list_3)-1]:
        print(list_3[0])
    else:
        print(list_3[0],list_3[len(list_3)-1])