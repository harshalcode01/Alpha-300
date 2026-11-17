def count_vowel_substrings(triumph):
    vowels = "aeiou"
    last = {"a": -1, "e": -1, "i": -1, "o": -1, "u": -1}

    x = 0
    y = 0

    for i in range(len(triumph)):
        ch = triumph[i]
        if ch not in vowels:
            x = i + 1
            for v in last:
                last[v] = -1
        else:
            last[ch] = i
            smallest = last["a"]
            for v in last:
                if last[v] < smallest:
                    smallest = last[v]
            if smallest >= x:
                y = y + (smallest - x + 1)
    return y
