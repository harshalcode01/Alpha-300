def harshal(triumph):
    n = len(triumph)
    counts = {}
    for ch in triumph:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    x = []
    for ch in counts:
        x.append(ch)
    y = merge_sort_by_count(x, counts)
    if counts[y[0]] > (n + 1) // 2:
        return ""
    result = [""] * n
    i = 0
    for ch in y:
        for j in range(counts[ch]):
            result[i] = ch
            i += 2
            if i >= n:
                i = 1
    return "".join(result)
