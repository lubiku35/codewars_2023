def geo_mean(nums, arith_mean):
    number = (arith_mean * (len(nums) + 1)) - sum(nums)  
    nums.append(number)
    x = 1
    for i in nums:
        x *= i
    return x ** (1/len(nums))


