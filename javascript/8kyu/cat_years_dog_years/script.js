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

console.log(humanYearsCatYearsDogYears(10));