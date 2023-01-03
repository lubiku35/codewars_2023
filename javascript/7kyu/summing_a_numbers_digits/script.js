function sumDigits(number) {
	let nums = Array.from(Math.abs(number).toString()).map(Number);
	let sum = 0
	for (const key in nums) {
		sum += nums[key]
	}
	return sum
}

