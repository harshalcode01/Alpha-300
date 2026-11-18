def harshal(triumph, counts):
    if len(triumph) <= 1:
        return triumph
    mid = len(triumph) // 2
    x = harshal(triumph[:mid], counts)
    y = harshal(triumph[mid:], counts)
    result = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if counts[x[i]] >= counts[y[j]]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    while i < len(x):
        result.append(x[i])
        i += 1
    while j < len(y):
        result.append(y[j])
        j += 1
    return result
