# Is there a vowel in there?

## Challenge Description

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (`a, e, i, o, u`).

If they are, change the array value to a string of that vowel.

Return the resulting array.

## Challenge Solutions

### Solution 01

```python
def is_vow(inp):
    return [chr(i) if i in [97, 101, 105, 111, 117] else i for i in inp]
```

**DESCRIPTION:**

effectivity