def min_min_max(arr):
    minimumm, maximum  = min(arr), max(arr)
    between = [i for i in range(minimumm + 1, maximum + 1) if i not in arr]
    return [minimumm, min(between), maximum]