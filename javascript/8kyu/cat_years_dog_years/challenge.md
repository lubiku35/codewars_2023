
# Cat years, Dog years

## Challenge Description

---

I have a cat and a dog.

I got them at the same time as kitten/puppy. That was `humanYears` years ago.

Return their respective ages now as [`humanYears`,`catYears`,`dogYears`]

NOTES:

- humanYears >= 1
- humanYears are whole numbers only

## Cat Years

- `15` cat years for first year
- `+9` cat years for second year
- `+4` cat years for each year after that

## Dog Years

- `15` dog years for first year
- `+9` dog years for second year
- `+5` dog years for each year after that

---

**References**

- [http://www.catster.com/cats-101/calculate-cat-age-in-cat-years](http://www.catster.com/cats-101/calculate-cat-age-in-cat-years)
- [http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html](http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html)

---

If you liked this Kata there is another [related one here](https://www.codewars.com/kata/cat-years-dog-years-2)

## Challenge Solutions


### Solution 01


```jsx
var humanYearsCatYearsDogYears = function(humanYears) {
	let years = [0, 0, 0]
	years[0] = humanYears
	for (let index = 0; index <= humanYears; index++) {
		if (index == 1) {
			years[2] = 15
			years[1] = years[2]
		}
		if (index == 2) {
			years[1] += 9 
			years[2] += 9
		}
		if (index > 2) {
			years[1] += 4 
			years[2] += 5
		}
	}
	return years;
}
```

**DESCRIPTION:**

In this challenge we just adding numbers as the description says, if it is just one year we add 15 years to both, if it is 2 years we add 9 years to both and for all the next years we adding for cats 4 years and 5 years for dogs. All of this is in range of the human years which is our input param.