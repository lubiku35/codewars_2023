function stray(numbers) {
	let x = numbers.reduce(function(a, b) {
	  return a ^ b;
	})
	return x
}

