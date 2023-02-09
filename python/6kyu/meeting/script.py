def meeting(s):
    names = [x.replace(':', ' ').upper() for x in s.split(";")]
    first_names = [name[0:name.index(' ')].upper() for name in names]
    last_names = [name[name.index(' ') + 1:].upper() for name in names]
    zipped = list(zip(last_names, first_names))
    sorted_zipped = sorted(zipped)
    x = ""
    for i in sorted_zipped:
        str = "("
        for j in i:
            if str.endswith(", "):
                str += j + ')'
            else:
                str += j + ', '
        x += str
    return x