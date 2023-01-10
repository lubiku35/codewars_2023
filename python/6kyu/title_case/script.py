
# SOLUTION FROM 2022

# def title_case(title, minor_words=''):
#     arr = minor_words.split(' ')
#     arr_2 = title.split(' ')
#     string = ''
#     for word in arr_2:
#         if word in arr:
#             string += word.lower() + ' '
#         else:
#             string += word.capitalize() + ' '
#     return string[0:-1]




def title_case(title, minor_words=''):
	minors = [i.lower() for i in minor_words.split(' ')]
	out = title.split(' ')[0].capitalize() + ' '
	for i in title.split(' ')[1:]:
		if i.lower() in minors: out += i.lower() + ' '
		else: out += i.capitalize() + ' '
	return out.strip()

print(title_case('The Wind In The Willows', 'The In'))