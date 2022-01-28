"""In this problem we have to remove the adjacent duplicate characters in the string. We have to do this while all the duplicates are removed"""
def remove_dup(S):
    i = 0
    length = len(S) - 1
    while i < (length):
        if S[i] == S[i+1]:
            try:
                S = S[:i] + S[i+2:]
                length -= 2
                if i > 1:    
                    i -= 2
                else:
                    i = -1
            except:
                pass
        i += 1
        #print(S)
    return S
print(remove_dup("abbaca"))
print(remove_dup('aaaaaaaa'))
"""In this solution, we will check if the next character is same as previous character. If it is, the we will remove those two characters and set the i such the it can check that newly formed string doesn't have the duplicates. Finally, we increment the character by 1"""
#first solution, but TIME LIMIT EXCEEDED
def remove_dup_TLE(S):
    cur_string = S
    sample_string = cur_string
    duplicate = True
    while duplicate:
        duplicate = False
        for i in range(len(cur_string) - 1):
            if cur_string[i] == cur_string[i+1]:
                try:
                    sample_string = cur_string[:i] + cur_string[i+2:]
                    duplicate = True
                except:
                    pass
        cur_string = sample_string
    return cur_string