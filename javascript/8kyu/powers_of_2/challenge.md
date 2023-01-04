
# Powers of 2

## Challenge Description

---

Complete the function that takes a non-negative integer `n` as input, and returns a list of all the powers of `2` with the exponent ranging from `0` to `n` ( inclusive ).

## Examples

```
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```

## Challenge Solutions


### Solution 01


```jsx
function powersOfTwo(n){
	let powers = [];
	for (let index = 0; index <= n; index++) powers.push(Math.pow(2, index));
	return powers;
}
```

**DESCRIPTION:**

Simple mathematic problem solved just by one for loop.