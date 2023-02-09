# Fix String Case

## Challenge Description


Complete the method which accepts an array of integers, and returns one of the following:

- `"yes, ascending"` - if the numbers in the array are sorted in an ascending order
- `"yes, descending"` - if the numbers in the array are sorted in a descending order
- `"no"` - otherwise

You can assume the array will always be valid, and there will always be one correct answer.

## Challenge Solutions


### Solution 01


```python
def is_sorted_and_how(arr):
	return 'yes, ascending' if arr == sorted(arr) else 'yes, descending' if arr == sorted(arr, reverse=True) else 'no'
```

**DESCRIPTION:**

In this challengem we just compare our input arr to the sorted one in ascending order and sorted one in descending order otherwise we return no