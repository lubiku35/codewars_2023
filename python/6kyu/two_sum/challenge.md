# Two Sum

---

## Challenge Description

---

Write a function that takes an array of numbers (integers for the 
tests) and a target number. It should find two different items in the 
array that, when added together, give the target value. The indices of 
these items should then be returned in a tuple / list (depending on your
 language) like so: `(index1, index2)`.

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 
or greater, and all of the items will be numbers; target will always be 
the sum of two different items from that array).

Based on: [http://oj.leetcode.com/problems/two-sum/](http://oj.leetcode.com/problems/two-sum/)

## Challenge Solutions

### Solution 01


```python
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target: return [i, j]
```

**DESCRIPTION:**

In this challenge by the indexes of numbers we have to compare numbers like this: if we got array of 3 numbers, these are the indexes [ [0, 1], [0, 2], [1, 2] ]… if we got array of 4 numbers, these are the indexes [ [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3] ] etc etc… we can do this by two for loops with some dependencies like in the solution.