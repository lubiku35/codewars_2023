def count_smileys(arr):
    valids = [':)', ';)', ':D', ';D', '-)', '-D', '~)', '~D']
    return len([x for x in arr if x[1::] in valids or x in valids])

