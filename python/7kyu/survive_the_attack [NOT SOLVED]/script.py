def bigger(x, y):
    return len(x) if len(x) >= len(y) else len(y)

def smaller(x, y):
    return len(x) if len(x) <= len(y) else len(y)


def is_defended(attackers, defenders):
    defenders_survivors = []
    attackers_survivors = []
    for i in range(bigger(attackers, defenders)):
        if i > smaller(attackers, defenders):
            x = defenders[i] - attackers[i] 
            if x > 0:
                defenders_survivors.append()