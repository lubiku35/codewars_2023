def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum([arr[i - 1] - arr[i] for i in range(1, len(arr))]) if len(arr) > 1 else 0
