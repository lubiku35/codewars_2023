
# Meeting

## Challenge Description

---

Given an array (arr) as an argument complete the function `countSmileys` that should return the total number of smiling faces.

Rules for a smiling face:

- Each smiley face must contain a valid pair of eyes. Eyes can be marked as `:` or `;`
- A smiley face can have a nose but it does not have to. Valid characters for a nose are `` or `~`
- Every smiling face must have a smiling mouth that should be marked with either `)` or `D`

No additional characters are allowed except for those mentioned.

**Valid smiley face examples:** `:) :D ;-D :~)`**Invalid smiley faces:**  `;( :> :} :]`

### Example

```
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

```

### Note

In case of an empty array return 0. You will not be tested with 
invalid input (input will always be an array). Order of the face (eyes, 
nose, mouth) elements will always be the same.

## Challenge Solutions


### Solution 01

---

```python
def count_smileys(arr):
    valids = [':)', ';)', ':D', ';D', '-)', '-D', '~)', '~D']
    return len([x for x in arr if x[1::] in valids or x in valids])
```

**DESCRIPTION:**

First of all, we got some cases when it is the right smiley, if we just count the last two characters of all possible right smileys, it is exactly the corresponding array of valids in our function. Then it is very simple, we just loop through our input param and check for every item if it’s last two character’s are in our array of valids.