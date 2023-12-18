import time
a = [1, 1, 1, 1, 0, 1, 0, 0]  # 5
b = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]  # 8
c = [0, 1, 1, 0, 0, 1, 0, 1, 1]  # 3
d = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]*100000  # 15


def max_ones(list_t):

    ''' Находит подстроку наибольшей длины из 1, если удалить какой-либо 0'''

    counter_1 = 0
    max_counter = 0
    flag = 0
    for i, e in enumerate(list_t):
        if e == 1:
            counter_1 += 1
            max_counter = max(max_counter, counter_1)

        if i == len(list_t)-1 and e == 0:
            continue
        else:
            if e == 0 and (list_t[i + 1] == 0 or list_t[i - 1] == 0):
                counter_1 = 0
                flag = 0
                continue
            if e == 0 and list_t[i + 1] == 1:
                if flag == 1:
                    counter_1 = len(list_t[point + 1:i])
                    point = i
                    flag = 2
                elif flag == 2:
                    counter_1 = len(list_t[point + 1:i])
                    flag = 0
                else:
                    flag = 1
                    point = i
        max_counter = max(max_counter, counter_1)
    return max_counter

start_time = time.time()  # время начала выполнения

print(max_ones(d))

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time} секунд")