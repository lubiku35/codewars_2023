function evenNumbers(array, number) {
	let evens = array.filter(function(x) {
	  return x % 2 === 0;
	})
	return evens.slice(-number)
}

