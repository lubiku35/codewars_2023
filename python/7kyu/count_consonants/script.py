def consonant_count(s):
    letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    counter = 0
    for i in s:
        if i not in letters and i.isalpha():
            counter += 1

    return counter
	



