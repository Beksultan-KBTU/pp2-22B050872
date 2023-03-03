import re

# problem = 1
# def text_match(text):
# 	patterns = 'a(b*)$'
# 	if re.search(patterns, text):
# 		return 'Found a match!'
# 	else:
# 		return ('Not matched!')
# print(text_match(str(input())))

# problem = 2
# def text_match(text):
# 	patterns = 'ab{2,3}'
# 	if re.search(patterns, text):
# 		return 'Found a match!'
# 	else:
# 		return ('Not matched!')
# print(text_match(str(input())))

# problem = 3
# def text_match(text):
# 	patterns = '[a-z]+_[a-z]+'
# 	if re.search(patterns, text):
# 		return 'Found a match!'
# 	else:
# 		return ('Not matched!')
# print(text_match(str(input())))

# problem = 4
# def text_match(text):
# 	patterns = '[A-Z][a-z]+'
# 	if re.search(patterns, text):
# 		return 'Found a match!'
# 	else:
# 		return ('Not matched!')
# print(text_match(str(input())))

# problem = 5
# def text_match(text):
# 	patterns = 'a.*b$'
# 	if re.search(patterns, text):
# 		return 'Found a match!'
# 	else:
# 		return ('Not matched!')
# print(text_match(str(input())))

# problem = 6
# def text_convert(text):
# 	patterns = '[ ,.]'
# 	new_text = re.sub(patterns, ':', text)
# 	return new_text
# print(text_convert(input()))

# problem = 7
# def text_match(text):
# 	patterns = '_([a-z])'
# 	camel_case = re.sub(patterns, lambda match: match.group(1).upper(), text) 
# 	return camel_case
# print(text_match(input()))

# problem = 8
# def text_match(text):
# 	patterns = '[A-Z][a-z]*'
# 	new_text = re.findall(patterns, text)
# 	return new_text
# print(text_match(input()))

# problem = 9
# def text_match(text):
# 	patterns = r'([a-z])([A-Z])'
# 	snake_case = re.sub(patterns, r'\1 \2', text)
# 	return snake_case
# print(text_match(input()))

# problem = 10
# def text_match(text):
# 	patterns = '([A-Z])'
# 	snake_case = re.sub(patterns, r'_\1', text).lower().lstrip('_') 
# 	return snake_case
# print(text_match(input()))