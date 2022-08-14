"""
FAILED
5. Longest Palindromic Substring
Medium

20605

1182

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def main(s):
    """
    Failed
    TIME LIMIT EXCEEDED
    if len(s) == 1:
        return s
    else:
        max_len = 1
        ans = s[0]
        for i in range(len(s) - 1):
            cur_str = s[i]
            temp = 0
            ans_str = ""
            for j in s[i+max_len:]:
                cur_str += j
                if cur_str == cur_str[::-1]:
                    temp = len(cur_str)
                    ans_str = cur_str
            if temp > max_len:
                max_len = temp
                ans = ans_str
    return ans
    """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #slow and steady hahaha
        
        #quick palindrome checker function    
        def palCheck(_str):
            return _str == _str[::-1]
        # if string is already a palindrome, just return it
        if palCheck(s):
            return s
        #empty string
        currLongest = ""
        for i in range(len(s)):
            #each letter in string could be start of longest palin substr
            testStr = ""
            #add letters till the end
            for j in range(i, len(s)):
                testStr += s[j]
                #if its a palindrome and it's longer than current longest
                if palCheck(testStr) and len(testStr) > len(currLongest):
                    #wipe current longest
                    currLongest = ""
                    #add current test str
                    currLongest += testStr
        #spit the longest out
        return currLongest

print(main("babad"))
print(main("cbbd"))
print(main("a"))