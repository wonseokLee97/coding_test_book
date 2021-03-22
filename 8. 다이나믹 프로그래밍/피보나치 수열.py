d = [0] * 100000000

def pivo(x):
    if x == 0 or x == 1:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = pivo(x - 1) + pivo(x - 2)

    return d[x]


print(pivo(900))
