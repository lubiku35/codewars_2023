def to_csv_text(array):
    string = ''
    for i in array: string += ",".join(str(x) for x in i) + '\n'
    return string[:-1]
