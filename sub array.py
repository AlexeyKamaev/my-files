def max_sequence(arr):

    while len(arr) > 3 and (arr[0] <= 0 or arr[-1] <= 0):
        if arr[0] <= 0:
            del arr[0]
        if arr[-1] <= 0:
            del arr[-1]

    maxi, cur = 0, 0

    for i, e in enumerate(arr):
        if e > 0:
            cur += e
            maxi = max(maxi, cur)
        if e < 0:
            if cur + e <= 0:
                cur = 0
            else:
                cur += e
            maxi = max(maxi, cur)

    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #6

print(max_sequence(arr))


def max_sequence(arr):
    maxi, cur = 0, 0

    for i, e in enumerate(arr):
        if e > 0:
            cur += e

        if e < 0:
            if cur + e <= 0:
                cur = 0
            else:
                cur += e
        maxi = max(maxi, cur)

    return maxi