n = 9
matrix = [
    [4, 5, 1, 2, 3, 4, 5, 1, 2],
    [2, 3, 7, 5, 1, 7, 3, 4, 5],
    [5, 1, 2, 3, 9, 5, 1, 8, 3],
    [3, 6, 5, 1, 2, 3, 4, 5, 1],
    [1, 2, 8, 4, 5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3, 9, 5, 1, 2],
    [2, 3, 4, 5, 1, 2, 3, 4, 5],
    [5, 1, 2, 3, 3, 5, 9, 2, 3],
    [3, 4, 5, 1, 2, 3, 4, 5, 1]
]

flag = 'YES'
def m_spin(matrix):
    res_matrix = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])
        res_matrix.append(cur_column[::-1])
    return res_matrix

for i in matrix:
    res = []
    for j in i:
        if j in res or j not in range(1, n + 1):
            flag = 'NO'

for i in m_spin(matrix):
    res = []
    for j in i:
        if j in res or j not in range(1, n + 1):
            flag = 'NO'

print(flag)

from matrices import matrix_power

X = matrix_power(matrix,-1)
for i in X:
    print(*i)


