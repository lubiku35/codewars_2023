
# Summing a number's digits

## Challenge Description

---

Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (**Input --> Output**)

```
10 --> 1
99 --> 18
-32 --> 5
```

Let's assume that all numbers in the input will be integer values.

## Challenge Solutions

---

### Solution 01

---

```jsx
function sumDigits(number) {
	let nums = Array.from(Math.abs(number).toString()).map(Number);
	let sum = 0
	for (const key in nums) {
		sum += nums[key]
	}
	return sum
}
```

**DESCRIPTION:**

Fisrt of all, variable nums contains array of our input parameter in absolute value changed to the string and splited by separate numbers, then we make a varible sum, loop through all numbers in our array and add their values to the our sum. We return the variable sum.  