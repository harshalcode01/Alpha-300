def harshal(triumph, x):
    counts = {}
    for ch in x:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    y = []
    for ch in triumph:
        if ch in counts:
            for i in range(counts[ch]):
                y.append(ch)
            counts[ch] = 0
    for ch in counts:
        for i in range(counts[ch]):
            y.append(ch)
    return "".join(y)

