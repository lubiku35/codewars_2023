
def alphabet_position(string):
    return " ".join(str(y) for y in [ord(x.lower()) - 96 for x in string if x.isalpha()])
    
