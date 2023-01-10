# String incrementer

## Challenge Descriptio

Your job is to write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

`foo -> foo1`

`foobar23 -> foobar24`

`foo0042 -> foo0043`

`foo9 -> foo10`

`foo099 -> foo100`

*Attention: If the number has leading zeros the amount of digits should be considered.*

## Challenge Solutions

### Solution 01

```python
def increment_string(strng):
	arr = []
	temp_num = ''
	temp_str = ''
	for i in range(len(strng)):
		if strng[i].isdigit():
			temp_num += strng[i] 
			if temp_str != '':
				arr.append(temp_str)
				temp_str = ''
		else:
			temp_str += strng[i]
			if temp_num != '':
				arr.append(temp_num)
				temp_num = ''
	
	if strng.isdigit():
		desired_num = int(strng) + 1
		arr_postfix = [x for x in strng]
		arr_desired_num = [x for x in str(desired_num)]

		lenght = len(arr_postfix) - len(arr_desired_num)
		x = 0
		out = ''
		for i in arr_postfix[:lenght]:
			out += i

		for i in arr_postfix[lenght:]: 
			i = arr_desired_num[x]
			x += 1
			out += i

		
		return out
	
	if arr == []:
		return strng + '1'
	else:
		prefix = ''.join(x for x in arr)
		postfix = strng.replace(prefix, '')
		desired_num = int(postfix) + 1
		arr_postfix = [x for x in postfix]
		arr_desired_num = [x for x in str(desired_num)]

		if len(arr_postfix) <= len(arr_desired_num):
			return prefix + str(desired_num)
		else:
			lenght = len(arr_postfix) - len(arr_desired_num)
			x = 0
			out = ''
			for i in arr_postfix[:lenght]:
				out += i

			for i in arr_postfix[lenght:]: 
				i = arr_desired_num[x]
				x += 1
				out += i

			return prefix + out
```

**DESCRIPTION:**

I hope that in next days will refactor the code and make more readable code for this solution