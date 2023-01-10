# Largest pair sum in array

## Challenge Description

Given a sequence of numbers, find the largest pair sum in the sequence.

For example

```
[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
```

Input sequence contains minimum two elements and every element is an integer.

## Challenge Solutions

### Solution 01

```python
import heapq
def largest_pair_sum(numbers): 
    return sum(heapq.nlargest(2, numbers))
```

**DESCRIPTION:**

For this challenge we use python library heapq and its function nlargest to find 2 largest numbers from our input param and return sum of this numbers.