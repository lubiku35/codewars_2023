
# No Loops 2 - You only need one

## Challenge Description

*** **No Loops Allowed** ***

You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. `x` can be either. Return `true` if the array contains the value, `false` if not. With strings you will need to account for case.

Looking for more, loop-restrained fun? Check out the other kata in the series:

[No Loops 1 - Small enough?](https://www.codewars.com/kata/no-loops-1-small-enough)

## Challenge Solutions

### Solution 01

```python
def check(a, x):
	return True if x in a else False
```

**DESCRIPTION:**

Challenge with very simple solution, just check if value x is in array a and return True if it is else return False.s