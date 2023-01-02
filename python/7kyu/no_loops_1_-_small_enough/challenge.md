
# No Loops 1 - Small enough ? 

## Challenge Description

*** **No Loops Allowed** ***

You will be given an array (a) and a limit value (limit). You must 
check that all values in the array are below or equal to the limit 
value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.

Do not use loops. Do not modify input array.

Looking for more, loop-restrained fun? Check out the other kata in the series:

[https://www.codewars.com/kata/no-loops-2-you-only-need-one](https://www.codewars.com/kata/no-loops-2-you-only-need-one) 

[https://www.codewars.com/kata/no-loops-3-copy-within](https://www.codewars.com/kata/no-loops-3-copy-within)

## Challenge Solutions

### Solution 01

---

```python
def small_enough(a, limit):
	return True if max(a) <= limit else False
```

**DESCRIPTION:**

We can’t loop through array so choosing maximum and compare this number with the limit will always work. If the maximum from the array is larger than out limit number function return **false** othervise **true**.