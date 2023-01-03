# Fix String Case

## Challenge Description

---

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

- make as few changes as possible.
- if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

For example:

```
solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
```

More examples in test cases. Good luck!

Please also try:

[Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)

[Simple remove duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)

## Challenge Solutions


### Solution 01

---

```python
def lowers(s):
	return len([x for x in s if x.islower()]) 

def uppers(s):
	return len([x for x in s if x.isupper()])

def solve(s):
    return s.lower() if lowers(s) >= uppers(s) else s.upper()
```

**DESCRIPTION:**

I’ve made three functions here, functions lowers() and uppers() returns number of occurences of lowercase/uppercase letters in our input param. In main function solve() just returning string in case what we need if lowers() returns bigger or equal number than uppers()