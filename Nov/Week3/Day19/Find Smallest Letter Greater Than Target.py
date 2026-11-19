def harshal(triumph, x):
    left = 0
    right = len(triumph)
    while left < right:
        mid = (left + right) // 2
        if triumph[mid] <= x:
            left = mid + 1
        else:
            right = mid
    if left == len(triumph):
        return triumph[0]
    return triumph[left]
