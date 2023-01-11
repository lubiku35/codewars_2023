# Flatten

## Challenge Description

Write a function that flattens an `Array` of `Array` objects into a flat `Array`.  Your function must only do one level of flattening.

```
flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]

```

## Challenge Solutions

### Solution 01

```python
def flatten(lst):
    arr = []
    for i in lst:
        if type(i) == str or type(i) == float or type(i) == int or type(i) == bool:
            arr.append(i)
            continue
        for item in i:
            arr.append(item)
    return arr
```

**DESCRIPTION:**

We define the output array and iterate through our input array if the item is string, float, integer or boolean just add the item and continue to the next iteration, if not iterate through the item and add to the arr all the items in item :)