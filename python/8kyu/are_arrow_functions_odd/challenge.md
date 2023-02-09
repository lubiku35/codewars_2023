# Are arrow functions odd?

## Challenge Description

Time to test your basic knowledge in functions! 
Return the odds from a list:

```
[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
```

## Challenge Solutions

### Solution 01

```python
def odds(arr):
    return list(filter(lambda x: x % 2 != 0, arr))
```

**DESCRIPTION:**

lambda function and more