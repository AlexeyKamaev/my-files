arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
arr2 = [
    [23,18,20,26,25],
    [24,22,3,4,4],
    [15,22,2,24,29],
    [18,15,23,28,28]
]
def snail(matrix):
    if matrix == [[]]:
        return []
    n, m = len(matrix), len(matrix[0])
    snail_list = []
    x, y = 0, 0
    dx, dy = 0, 1
    count = 2
    snail_list.append(matrix[x][y])
    matrix[x][y] = ''

    while count <= n*m :
        if 0 <= x + dx <= n -1 and 0 <= y + dy <= m -1 and matrix[x + dx][y + dy] != '':
            snail_list.append(matrix[x + dx][y + dy])
            matrix[x + dx][y + dy] = ''
            count += 1
            x += dx
            y += dy
        else:
            if dy == 1:
                dy = 0
                dx = 1
            elif dx == 1:
                dx = 0
                dy = -1
            elif dy == -1:
                dy = 0
                dx = -1
            elif dx == -1:
                dx = 0
                dy = 1
    return snail_list

print(snail(arr2))