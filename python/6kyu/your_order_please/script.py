def order(sentence):
    x = ""
    if sentence != "":
        x = sentence.split(' ')

    indexes = [x for x in range(1, len(x) + 1)]
    for i in x:
        for letter in i:
            if letter.isdigit():
                indexes.insert(int(letter) - 1, i)
                indexes.remove(int(letter)) 

    return " ".join(indexes)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))