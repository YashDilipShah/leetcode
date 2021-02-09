true_string = "{{a;lkdsfj(ajsdlfk;j){ajlksdf[akl;jsdf(a;lksdjfkl;asj)]}}}"
false_string = "{{a;lkdsfj(ajsdlfk;j){ajlksdf[akl;jsdf(a;lksd{]jfkl;asj)]}}}"
def parenthesis_check(string):
	open = ["(", "{", "["]
	letters = [i for i in string]
	stack = []
	for i in letters:
		if i in open:
			stack.append(i)
		elif i == ")":
			try:
				if stack.pop() == "(":
					continue
				else:
					return False
			except:
				return False
		elif i == "]":
			try:
				if stack.pop() == "[":
					continue
				else:
					return False
			except:
				return False
		elif i == "}":
			try:
				if stack.pop() == "{":
					continue
				else:
					return False
			except:
				return False
	if len(stack) == 0:
		return True
	else:
		return False

print(parenthesis_check(true_string))
print(parenthesis_check(false_string))
print(parenthesis_check("())"))
print(parenthesis_check("["))
print(parenthesis_check('[](){([[[]]])}'))