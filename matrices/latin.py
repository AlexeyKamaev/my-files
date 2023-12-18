n = 5
matrix = [
    [4, 1, 1, 2, 3],
    [2, 3, 4, 1, 1],
    [1, 1, 2, 3, 4],
    [3, 4, 1, 1, 2],
    [1, 2, 3, 4, 1]]
flag = 'YES'
res = []

for i in range(n):
    matrix[i] = sorted(matrix[i])
    if matrix[i] not in res:
        res.append(matrix[i])
    else:
        continue
print(res)
if len(res) != 1 or len(res) == 1 and len(matrix) == 2:
    flag = 'NO'

nums = []
for i in res[0]:
    if i not in nums:
        nums.append(i)

    else:
        flag = 'NO'
if matrix[0] == matrix[-1]:
    flag = 'NO'


print(flag)
