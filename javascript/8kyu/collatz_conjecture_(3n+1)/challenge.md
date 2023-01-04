
# Collatz Conjecture (3n+1)

The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that 
applying the following algorithm to any number we will always eventually reach one:

```
[This is writen in pseudocode]
if(number is even) number = number / 2
if(number is odd) number = 3*number + 1

```

**Task**

Your task is to make a function `hotpo` that takes a positive `n` as input and returns the number of times you need to perform this algorithm to get `n = 1`.

**Examples**

```
hotpo(1) returns 0
(1 is already 1)

hotpo(5) returns 5
5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(6) returns 8
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

hotpo(23) returns 15
23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

```

**References**

- Collatz conjecture wikipedia page: [https://en.wikipedia.org/wiki/Collatz_conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

## Challenge Solutions


### Solution 01

```jsx
var hotpo = function(n) {
    if(n == 0) return 0; //Optional Handler to n = 0
    counter = 0

	while (n != 1) {
		if (n % 2 == 0) {
			n = n / 2
			counter += 1 
		}
		else {
			n = 3 * n + 1
			counter += 1 
		}
	}
	return counter
}
```

**DESCRIPTION:**

Challenge contains three problems you have to handle, first is simple, just do the next two problems while number is not equals to 1. Other two problems are just mathematics, if remainder after dividing number by two is zero, number equals number divided by 2 else number equals number times 3 plus 1

Also we have to handle counter which increments everytime we do one of the operations (dividing by 2 or, times 3 plus 1)