# Meeting

## Challenge Description

```
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
```

Could you make a program that

- makes this string uppercase
- gives it sorted in alphabetical order by last name.

When the last names are the same, sort them by first name.
Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function `meeting(s)` will be:

```
"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
```

It can happen that in two distinct families with the same family name two people have the same first name too.

### Notes

- You can see another examples in the "Sample tests".

## Challenge Solutions

### Solution 01

```python
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
```

**DESCRIPTION:**

uff kinda cool