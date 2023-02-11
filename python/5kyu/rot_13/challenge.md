# ROT13

## Challenge Descriptio

How can you tell an extrovert from an introvert at NSA?Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?According to Wikipedia, [ROT13](http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

```
"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
```

## Challenge Solutions

### Solution 01

```python
def rot13(string):
	out = ""
	for i in [x for x in string]:
		if i.isalpha():
			if (ord(i) >= 65 and ord(i) <= 77) or (ord(i) >= 97 and ord(i) <= 109): out += chr(ord(i) + 13)
			else: out += chr(ord(i) - 13)
		else: out += i
	return out
```

**DESCRIPTION:**

not best not worst solution