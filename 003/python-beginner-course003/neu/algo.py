def ggt(a, b):
    if a == b:
        return a
    elif a < b:
        return ggt(a, b - a)
    else:
        return ggt(a - b, b)


def euklid(a, b):
    if b % a == 0:
        return a
    else:
        return euklid(b % a, a)
