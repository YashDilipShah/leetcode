"""In this probem, we have to return the outer most parenthesis of the string given. """
def remove(string):
    stack = []
    ans = ""
    for i in string:
        if i == "(":
            stack.append(i)
            if len(stack) > 1:
                ans += i
        else:
            if len(stack) > 1:
                ans += i
                stack.pop()
            else:
                stack.pop()
    return ans
print(remove('(()())(())'))
print(remove('(()())(())(()(()))'))
"""For this problem, we will maintain a stack. If the stack is empty, means we have encountered an outer parenthesis. In that case, we won't add the characters in our answer string. Otherwise, we will add the characters as it is in the answer string. """