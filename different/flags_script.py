flags = []
def flags_maker(r = 3):
    X = 1
    x = 1
    for i in range(r):
        if X == 1:
            x += 8
            flags.append(x)
            X = -X
        else:
            x += 10
            flags.append(x - 2)
            X = -X
    return flags