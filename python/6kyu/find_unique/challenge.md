# Find the unique number

## Challenge Description

There is an array with some numbers. All numbers are equal except for one. Try to find it!

```
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

1. Find the unique number (this kata)
2. [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

## Challenge Solutions

### Solution 01

```python
def find_uniq(arr):
	arr = sorted(arr, reverse=True)
	return max(arr) if arr[0] != arr[1] and arr[0] != arr[2] else min(arr)
```

**DESCRIPTION:**

My solution was that we take minimum and maximum and these numbers we compare to the sorted array in descending order, so if our maximum if different than second and third item in the sorted array in descending order it will return maximum else we just return minimum