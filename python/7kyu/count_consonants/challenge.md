# Count consonants

## Challenge Description

Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels `a, e, i, o, u`.

## Challenge Solutions

### Solution 01

```python
def consonant_count(s):
    letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    counter = 0
    for i in s:
        if i not in letters and i.isalpha():
            counter += 1

    return counter
```

**DESCRIPTION:**

Just iterate through string and add to counter if letter is alpha and not in the list`