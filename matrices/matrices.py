A = [
    [1, 0],
    [4, 1]]
B = [
    [1, 0],
    [4, 1]]
X = [
    [2, 5],
    [6, 7],
    [1, 8]]
Y = [
    [1, 2, 1],
    [0, 1, 0]]
P = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
k = 2

# A,B = matrix_make()
# print(*sum_matrix(A, B))
# n,m = [int(i) for i in input().split()]
# A = [[int(i) for i in input().split()] for _ in range(n)]
# for i in mul_matrix(X,Y):
# print(*i)

# for x in range(len(A)):
#    for y in range(len(A)):
#        print(str(mul_matrix(A,B)[x][y]).ljust(3), end = '')
#    print()

#if type(result) == str:
#    print(result)
#else:
#    for x in range(len(result)):
#        for y in range(len(result[0])):
#            print(str(result[x][y]).ljust(4), end = '')
#        print()


def matrix_make():

    n, m = [int(i) for i in input('Введите n и m через пробел:\n').split()]
    A = [[int(i) for i in input(f'Введите {m} элеметнов строки {k + 1} для матрицы А через пробел:\n').split()] for k in
         range(n)]
    input()

    B = [[int(i) for i in input(f'Введите {m} элеметнов строки {k + 1} для матрицы А через пробел:\n').split()] for k in
         range(n)]

    return A, B
def sum_matrix(A: list, B: list) -> list or str:
    '''Суммирование матриц'''
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        return f'Выполнение операции суммирования матриц невозможно'
    n, m = len(A), len(A[0])
    C = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C
def mul_matrix(A: list, B: list) -> list or str:
    '''Перемножение матриц'''
    n = len(A)
    m = len(B[0])
    if n != m:
        return f'Выполнение операции умножения матриц невозможно'
    C = [[0 for j in range(n)] for i in range(n)]
    x = len(A[0])

    for i in range(n):
        for j in range(n):
            for k in range(x):
                C[i][j] += A[i][k] * B[k][j]
    return C
def matrix_power(A: list, p=1) -> list or str:
    '''Возведение матрицы в степень'''
    Ap = A
    try:
        for _ in range(p - 1):
            Ap = mul_matrix(Ap, A)
        return Ap
    except:
        return f'Выполнение операции возведения матрицы в степень невозможно'
def det_mat(A: list ) -> int or float or str:
    if len(A) != len(A[0]):
        return f'Для матрицы вида {len(A)}x{len(A[0])} определитель посчитать невозможно'
    total = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return total
def mat_turn(A: list, t =1)-> list:
    ''' Поворачивает матрицу по часовой стрелке t раз,'''
    res_matrix = []
    t = t - 4 * (t // 4)
    if t <= 0 or t % 4 == 0:
        return A

    for j in range(len(A[0])):
        cur_column = []
        for i in range(len(A)):
            cur_column.append(A[i][j])
        res_matrix.append(cur_column[::-1])
    if t == 1:
        return res_matrix
    else:
        for i in range(1,t):
            res_matrix = mat_turn(res_matrix)
        return res_matrix
