def meeting(s):
    names = [x.replace(':', ' ') for x in s.split(";")]
    first_names = [name[0:name.index(' ')].upper() for name in names]
    last_names = [name[name.index(' ') + 1:].upper() for name in names]
    dicted = dict(zip(last_names, first_names))
    sorted_dict = sorted(dicted.items())
    x = ""
    for i in sorted_dict:
        str = "("
        for j in i:
            if str.endswith(", "):
                str += j + ')'
            else:
                str += j + ', '
        x += str
    return x

print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:Stan;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))
    #   (ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS))

print(meeting("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell"))
    #   (BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL))

print(meeting("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern"))
    #   (ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)
