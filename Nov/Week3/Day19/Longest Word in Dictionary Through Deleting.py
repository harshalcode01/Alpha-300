def harshal(triumph, x):
    y = ""
    for word in x:
        if len(word) < len(y):
            continue
        i = 0
        for ch in triumph:
            if i < len(word) and word[i] == ch:
                i += 1
        if i == len(word):
            if len(word) > len(y) or word < y:
                y = word
    return y

