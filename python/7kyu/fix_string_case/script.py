def lowers(s):
	return len([x for x in s if x.islower()]) 

def uppers(s):
	return len([x for x in s if x.isupper()])

def solve(s):
    return s.lower() if lowers(s) >= uppers(s) else s.upper() 



