def pythagorean_triple(integers):
    maximum = max(integers)
    integers.remove(maximum)
    return True if maximum ** 2 == integers[0] ** 2 + integers[1] ** 2 else False