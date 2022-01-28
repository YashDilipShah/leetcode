"""459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Accepted
129,775
Submissions
307,854"""
def repeatedSubstringPattern(s):
    if len(s) == 1:
        return False
    elif s.count(s[0]) == len(s):
        return True
    else:
        for i in range(1, (len(s) // 2) + 1):
            substr = s[:i]
            if (s.startswith(substr) and s.endswith(substr)):
                if s == substr * (len(s) // len(substr)):
                    return True
        return False


print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))