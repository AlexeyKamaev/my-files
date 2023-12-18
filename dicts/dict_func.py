result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]  # 3 списка

dict = {}
for i in range(int(input())):
    s = input().split(': ')
    dict.setdefault(s[0].lower(), s[1])

for i in range(int(input())):
    print(dict.get(input().lower(), 'Не найдено'))

d = {}  # метод dict.fromkeys()
for _ in range(int(input())):
    country, *cities = input().split()
    d.update(dict.fromkeys(cities, country))
for _ in range(int(input())):
    print(d[input()])

cont = {}  # длеам {ключ: [a,b,c]}
for _ in range(int(input())):
    num, name = input().lower().split()
    cont.setdefault(name, []).append(num)
for _ in range(int(input())):
    print(*cont.get(input().lower(), ['абонент не найден']))
