"""821. Shortest Distance to a Character
Easy

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

 

Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.

"""
def shortestToChar(S, C):
    pos = []
    ans = []
    for i in range(len(S)):
        if S[i] == C:
            pos.append(i)
    
    for i in range(len(S)):
        ans.append(min([abs(j - i) for j in pos]))
    
    return ans

print(shortestToChar(S = "loveleetcode", C = 'e'))