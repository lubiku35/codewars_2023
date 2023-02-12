def add_all(lst): 
    x = lst[0]
    cumulatives = []
    for i in range(1, len(lst)):
        x += lst[i]
        cumulative_sum = x
        cumulatives.append(cumulative_sum) 
    return cumulatives

print(add_all([1,2,3,4,5]))