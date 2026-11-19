def harshal(triumph, x):
    y = 0
    while y < len(triumph) and y < len(x):
        if triumph[y] < x[y]:
            return -1
        if triumph[y] > x[y]:
            return 1
        y += 1
    if len(triumph) < len(x):
        return -1
    if len(triumph) > len(x):
        return 1
    return 0


