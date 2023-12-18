limit = 200

l = []

for i in range(1, limit + 1):
    for j in range(i, limit + 1):
        cubes_sum = i ** 3 + j ** 3
        for k in range(i + 1, limit + 1):
            for p in range(k, limit + 1):
                if cubes_sum == (k ** 3 + p ** 3):
                    l.append(cubes_sum)

print(list(sorted(l)[:2]))