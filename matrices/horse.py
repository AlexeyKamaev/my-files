n = 8
matrix = [['.' for _ in range(n)] for _ in range(n)]
collum = 'abcdefgh'
line = '87654321'
lead = []

for i in input():
    if i.isalpha():
        col = collum.index(i)
    else:
        row = line.index(i)

matrix[row][col] = 'N'

potential = [[row-1,col-2],[row+1,col-2],[row+1,col+2],[row-1,col+2],
         [row+2,col-1],[row+2,col+1],[row-2,col-1],[row-2,col+1]]

for i in potential:
    if i[0] < 0 or i[1] < 0 or i[0] > n-1 or i[1] > n-1:
        continue
    else:
        lead.append(i)
for i in lead:
    matrix[i[0]][i[1]] = '*'

for i in matrix:
    print(*i, sep = ' ')