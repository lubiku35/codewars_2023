# Mean Means

## Challenge Description

## Introduction

Take a list of `n` numbers `a1, a2, a3, ..., aN` to start with.

**Arithmetic mean** (or average) is the sum of these numbers divided by `n`.

**Geometric mean** (or average) is the product of these numbers taken to the `n`th root.

### Example

List of numbers: `1, 3, 9, 27, 81`

- `n = 5`
- Arithmetic mean = `(1 + 3 + 9 + 27 + 81) / 5 = 121 / 5 = 24.2`
- Geometric mean = `(1 * 3 * 9 * 27 * 81) ^ (1/5) = 59049 ^ (1/5) = 9`

## Task

You will be given a list of numbers and their arithmetic mean. **However, the list is missing one number.**
 Using this information, you must figure out and return the geometric 
mean of the FULL LIST, including the number that's missing.

## Challenge Solutions

### Solution 01

```python
def geo_mean(nums, arith_mean):
    number = (arith_mean * (len(nums) + 1)) - sum(nums)  
    nums.append(number)
    x = 1
    for i in nums:
        x *= i
    return x ** (1/len(nums))
```

**DESCRIPTION:**

Explore the mathematics behind this solution