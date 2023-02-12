def data_reverse(data):
    out = []
    x = [data[i:i + 8] for i in range(0, len(data), 8)]
    for i in x[::-1]:
        out += i
    return out
