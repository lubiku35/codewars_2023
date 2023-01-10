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
	




