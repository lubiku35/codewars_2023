def rot13(string):
	out = ""
	for i in [x for x in string]:
		if i.isalpha():
			if (ord(i) >= 65 and ord(i) <= 77) or (ord(i) >= 97 and ord(i) <= 109): out += chr(ord(i) + 13)
			else: out += chr(ord(i) - 13)
		else: out += i
	return out