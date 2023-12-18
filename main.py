def find_subarr_maxsum(arr):
    while len(arr) > 3 and (arr[0] <= 0 or arr[-1] <= 0):
        if arr[0] <= 0 and arr[0]<arr[1]:
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



    r = []
    point = 0
    sumr = 0

    for i, e in enumerate(arr):
        sumr+= e
        if sumr == maxi:
            r.append(arr[point:i+1])
            point = i
            sumr = 0

    print( [r, maxi])




array = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #[4, -1, 2, 1]


find_subarr_maxsum(array)