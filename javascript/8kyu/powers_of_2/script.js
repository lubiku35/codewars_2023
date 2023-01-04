function powersOfTwo(n){
	let powers = [];
	for (let index = 0; index <= n; index++) powers.push(Math.pow(2, index));
	return powers;
}
