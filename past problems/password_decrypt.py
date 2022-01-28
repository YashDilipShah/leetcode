import flask

def decryptPassword(s):
    stack = []
    password_started = False
    while not password_started:
        try:
            stack.append(int(s[0]))
            s = s[1:]
        except:
            password_started = True
    s = [i for i in s]
    for i in range(len(s)):
        if s[i] == '*':
            s[i-1], s[i-2] = s[i-2], s[i-1]
            s[i] = ''
        elif s[i] == '0':
            s[i] = str(stack.pop())
    
    return ''.join(s)

print(decryptPassword('51Pa*0Lp*0e'))
print(decryptPassword('pTo*Ta*O'))
print(decryptPassword('1234500000'))