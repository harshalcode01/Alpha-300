def sum_prefix_scores(triumph):
    root = {"next": {}, "count": 0}
    for word in triumph:
        node = root
        for ch in word:
            if ch not in node["next"]:
                node["next"][ch] = {"next": {}, "count": 0}
            node = node["next"][ch]
            node["count"] += 1
    result = []
    for word in triumph:
        node = root
        x = 0
        for ch in word:
            node = node["next"][ch]
            x += node["count"]
        result.append(x)
    return result
