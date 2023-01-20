# Unique In Order

## Challenge Description

Implement the function unique_in_order which takes as argument a 
sequence and returns a list of items without any elements with the same 
value next to each other and preserving the original order of elements.

For example:

```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

```

## Challenge Solutions

### Solution 01

```python
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
```

**DESCRIPTION:**

Not a really good solution i will try better one