n,m  = [int(i) for i in input().split()]

def spiral_matrix(n,m):
    matrix = [[0 for j in range(m)] for i in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    matrix[x][y] = 1
    count = 2
    while count <= n*m :
        if 0 <= x + dx <= n -1 and 0 <= y + dy <= m -1 and matrix[x + dx][y + dy] == 0:
            matrix[x + dx][y + dy] = count
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
    return matrix


for i in range(n):
    for j in range(m):
        print(str(spiral_matrix(n,m)[i][j]).ljust(3), end = ' ')
    print()
