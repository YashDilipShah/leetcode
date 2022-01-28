"""387. First Unique Character in a String
Easy

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

 

Note: You may assume the string contains only lowercase English letters.
"""
def firstUniqChar(s):
    if s == "":
        return -1
    letters = set(s)
    ans = []
    print(letters)
    for i in letters:
        if s.count(i) == 1:
            ans.append(s.index(i))
    if len(ans) == 0:
        return -1
    else:
        return min(ans)
print(firstUniqChar("leetcode"))