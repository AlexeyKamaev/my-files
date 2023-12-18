from functools import reduce
def task_1():
    '''Задача 1: Скрабл'''
    a = 'qwertyuiopasdfghjklzxcvbnm'
    points_en = {
        1: 'AEIOULNSTR',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JZ',
        10: 'QZ'}
    points_ru = {
        1: 'АВЕИНОРСТ',
        2: 'ДКЛМПУ',
        3: 'БГЁЬЯ',
        4: 'ЙЫ',
        5: 'ЖЗХЦЧ',
        8: 'ШЭЮ',
        10: 'ФЩЪ'}

    text = input('Введите слово:\n')
    total = 0

    if text.lower()[0] in a:
        for c in text.upper():
            for k, v in points_en.items():
                if c in v:
                    total += k
                    break
        return total
    else:
        for c in text.upper():
            for k, v in points_ru.items():
                if c in v:
                    total += k
                    break
        return total
def task_2():
    '''Задача 2: Рюкзак'''

    ves = float(input('Введите вес в кг:\n')) * 1000
    result = []

    things = {'зажигалка': 20, 'компас': 100,
              'фрукты': 500, 'рубашка': 300,
              'термос': 1000, 'аптечка': 200,
              'куртка': 600, 'бинокль': 400,
              'удочка': 1200, 'салфетки': 40,
              'бутерброды': 820, 'палатка': 5500,
              'спальный мешок': 2250, 'жвачка': 10}
    while len(things) != 0:
        for k, v in things.items():
            if v == max(things.values()):
                if ves - v >= 0:
                    ves -= v
                    result.append(k)
                    del things[k]
                    break
                else:
                    del things[k]
                    break
    result.sort()
    return result
def task_3():
    '''Задача 3. Email-адреса'''

    emails = {
        'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
        'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
        'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
        'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
        'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
        'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

    print(sorted([i + '@' + email for email, name in emails.items() for i in name]))
def task_4():
    '''Задача 4: Права доступа'''
    tasks = {}
    do = list()
    for _ in range(int(input())):
        k, *v = input().split()
        tasks[k] = v
    for _ in range(int(input())):
        v, k = input().split()
        if v[0].upper() == 'E':
            x = 'X'
        else:
            x = v[0].upper()
        do.append((k, x))
    for i in do:
        if i[1] in tasks.get(i[0]):
            print('OK')
        else:
            print('Access denied')
def task_5():
    '''Задача 5: Продажи'''
    buyers = {}

    for _ in range(int(input())):
        name, item, price = input().split()
        price = int(price)
        buyers.setdefault(name, {})
        buyers[name][item] = price + buyers[name].get(item, 0)

    for name in sorted(buyers):
        print(f'{name}:')
        for item in sorted(buyers[name]):
            print(item, buyers[name][item])
def task_6(values):
    '''Задача 6: Объединение словарей'''
    result = {}
    for i in values:
        for k,v in i.items():
            if result.get(k) is None:
                result.setdefault(k,set([v]))
            else:
                result[k] = result[k] | set([v])
    return result
def task_7():
    '''Задача 7: Коты и владельцы'''
    cats = [('Мартин', 5, 'Алексей', 'Егоров'),
            ('Фродо', 3, 'Анна', 'Самохина'),
            ('Вася', 4, 'Андрей', 'Белов'),
            ('Муся', 7, 'Игорь', 'Бероев'),
            ('Изольда', 2, 'Игорь', 'Бероев'),
            ('Снейп', 1, 'Марина', 'Апраксина'),
            ('Лютик', 4, 'Виталий', 'Соломин'),
            ('Снежок', 3, 'Марина', 'Апраксина'),
            ('Марта', 5, 'Сергей', 'Колесников'),
            ('Буся', 12, 'Алена', 'Федорова'),
            ('Джонни', 10, 'Игорь', 'Андропов'),
            ('Мурзик', 1, 'Даниил', 'Невзоров'),
            ('Барсик', 2, 'Виталий', 'Соломин'),
            ('Рыжик', 7, 'Владимир', 'Медведев'),
            ('Матильда', 8, 'Андрей', 'Белов'),
            ('Гарфилд', 3, 'Александр', 'Березуев')]
    data = {}

    for i, e in enumerate(cats):
        cat = e[0] + ', ' + str(e[1])
        data.setdefault(e[2] + ' ' + e[3], []).append(cat)
    name = input().title()
    a = data.get(name, 'нет сведений о животных')
    print(name + ' : ' + str(a))
def task_8():
    '''Задача 8: Редкое слово'''
    n = input().lower()
    dict = {}
    ss = '.,!?:;!@#$%^&*(^&*()_+?><,./-'
    l = []
    for i in ss:
        n = n.replace(i, '')
    n = n.split()

    for i in n:
        dict.setdefault(i, n.count(i))

    for k, v in dict.items():
        if v == min(dict.values()):
            l.append(k)
    l.sort()
    print(l[0])
def task_9():
    '''Задача 9: Дубликаты'''
    n = input().split()
    for i, e in enumerate(n):
        if e in n[:i]:
            print(f'{e}_{n[:i].count(e)}', end=' ')
        else:
            print(e, end=' ')
def task_10():
    '''Задача 10: Анаграммы'''
    a, b = input(), input()
    dict_a = {i: a.count(i) for i in a}
    dict_b = {i: b.count(i) for i in b}

    print('YES' if dict_a == dict_b else 'NO')
def task_11():
    '''Задача 11: Расшифровка'''
    s = input()
    d = {}
    d_s = {}
    for i in s:
        d_s.setdefault(i, str(s.count(i)))
    for _ in range(int(input())):
        k, v = input().split(': ')
        d.setdefault(k, v)
    for k, v in d.items():
        for x, y in d_s.items():
            if v == y:
                s = s.replace(x, k)
    print(s)
def task_12():
    '''Задача 12: Запрос'''
    parametr = {'course': 'python', 'lesson': 2, 'challenge': 17}
    p_s = sorted(parametr)
    r = ''
    for k in p_s:
        r += k+'='+str(parametr[k])+'&'
    print(r.strip('&'))



def prepare_task_1():
    '''1. Напишите функцию, которая ставит большие буквы в начале каждого предложения: "jack has an apple. mary has an orange."
    → "Jack has an apple. Mary has an orange."'''

    string = 'jack has an apple. mary has an orange.    i wanna cry a bit'
    r = ''
    flag = False
    for i,c in enumerate(string):
        if flag:
            if c in ' .':
                r += c
                continue
            else:
                r += c.upper()
                flag = False
        else:
            if i == 0:
                r += c.upper()
            elif c in '.?!':
                r += c
                flag = True
            else:
                r += c
    return r
def prepare_task_2():
    '''2. Напишите функцию, которая возвращает самый частый элемент в массиве
    [1,2,1,3,2,1] → 1'''
    array = [1,2,1,3,2,1,7,7,7,7,7,7,7]
    return sorted(array,key = lambda x: array.count(x))[-1]
def prepare_task_3():
    '''3. Напишите функцию, которая принимает на вход список имен файлов, и возвращает словарь с количествами файлов каждого типа
["image1.jpg", "image2.jpg", "presentation.pptx"] → {"jpg": 2, "pptx": 1}'''
    files = ["image1.jpg", "image2.jpg", "presentation.pptx"]
    r = {}
    for i in files:
        i = i.split('.')
        r.setdefault(i[1], 0)
        r[i[1]] += 1
    return r
def prepare_task_4():
    '''4. Напишите функцию fizzbuzz, которая заменяет все элементы в списке, которые делятся на 3 на "fizz",
    которые делятся на 5 на "buzz", а которые делятся на 15 на "fizzbuzz"

    [1, 3, 4, 5, 10, 15, 20, 21] →
    [1, "fizz", 4, "buzz", "buzz", "fizzbuzz", "buzz", "fizz"]'''

    array = [1, 3, 4, 5, 10, 15, 20, 21,45,8]
    return list(map(lambda x: [['fizz','buzz'],[ 0 ,'fizzbuzz']][x%15 == 0][x%5 == 0] if x%3 == 0 or x%5 == 0 else x, array))
def prepare_task_5():
    '''5. Напишите функцию, которая получает на вход список этажей, на которых побывал лифт,
     и возвращает, сколько всего этажей он проехал
    [1, 5, 2, 7, 9, 1] → 22'''
    from functools import reduce
    array = [1, 5, 2, 7, 9, 1]
    t = 0
    for i in range(len(array)-1):
        t+= abs(array[i+1] - array[i])
    return t
def prepare_task_6():
    '''Напишите функцию, которая принимает список, состоящих из чисел и строк,
    и возвращает список состоящий сначала из чисел в порядке возрастания,
     а затем из строк в алфавитном порядке
    [5, "abc", 2, 1, "d", "ac"] → [1, 2, 5, "abc", "ac", "d"] '''
    array = [5, "abc", 2, 1, "d", "ac"]
    return sorted(array, key = lambda x: (str(type(x)), x))

def dir_reduc(arr):
    d = {'N':'NORTH','E':'EAST','W':'WEST','S':'SOUTH'}
    l = ''.join([x[0] for x in arr])
    while 'NS' in l or 'SN' in l or 'WE' in l or 'EW' in l:
        l = l.replace('NS', '')
        l = l.replace('SN', '')
        l = l.replace('EW', '')
        l = l.replace('WE', '')
    result = []
    for i in l:
        result.append(d.get(i,None))
    return result
def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):
        if num%n==0:
            return False
    return True
def issqrt(num,d):
    for i in range(max(d), max(d)*4):
        i2 = i * i
        if i2 == num:
            return True
        elif i2 > num:
            break
    return False

def list_squared(m, n):
    array = [i for i in range(m,n+1)]
    r = []
    for x in array:
        d = {1,x}
        if not isprime(x):
            for y in range(2, x//2+1):
                if x % y == 0:
                    d.add(y)
                    d.add(x % y)
                if x % y >= x//2
                    break
        k = reduce(lambda a,b : a + b**2, d)
        if issqrt(k,d):
            r.append([x,k])
            print(r)
    return r

a = 1
b = 100000
print(list_squared(a,b))