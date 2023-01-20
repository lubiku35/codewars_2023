def unique_in_order(sequence):
    x = []
    for i in sequence:

        if len(str(i)) != 1 and type(i) == str:
            for j in i:
                x.append(j)
        else:
            x.append(i)

    temp = []
    counter = 0
    for i in x:
        if temp == []:
            temp.append(i)
        else:
            if i == temp[counter]:
                continue
            else:
                temp.append(i)
                counter += 1
    return temp


print(unique_in_order('AAAABBBCCDAABBB')) 
# == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))
#  == ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, -3]))
#  == [1, 2, 3]
print(unique_in_order((1, 2, 2, 3, 3)))
#   == [1, 2, 3]