def harshal(triumph):
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
    result = []
    for ch in y:
        for i in range(counts[ch]):
            result.append(ch)
    return "".join(result)

