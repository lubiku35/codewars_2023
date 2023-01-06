# Sum of differences in array


## Challenge Description

Your task is to sum the differences between consecutive pairs in the array in descending order.

## Example

```
[2, 1, 10]  -->  9
```

In descending order: `[10, 2, 1]`

Sum: `(10 - 2) + (2 - 1) = 8 + 1 = 9`

If the array is empty or the array has only one element the result should be `0` (`Nothing` in Haskell, `None` in Rust).

## Challenge Solutions

## Challenge Solutions

### Solution

```python
def to_csv_text(array):
    string = ''
    for i in array: string += ",".join(str(x) for x in i) + '\n'
    return string[:-1]
```

**DESCRIPTION:**

Pretty good challenge, we have to hadle more things here, first is changing numbers to string format and adding after everyone “,”, then after every iteration add “\n” but return without last “\n”