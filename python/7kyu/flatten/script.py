def flatten(lst):
    arr = []
    for i in lst:
        if type(i) == str or type(i) == float or type(i) == int or type(i) == bool:
            arr.append(i)
            continue
        for item in i:
            arr.append(item)
    return arr




