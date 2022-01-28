"""409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1

Example 3:

Input: s = "bb"
Output: 2

 

Constraints:

    1 <= s.length <= 2000
    s consits of lower-case and/or upper-case English letters only.

"""
def main(s):
    from collections import Counter
    s = Counter(s)
    ans = 0
    odd = 0
    for i in s.values():
        if i % 2 == 0:
            ans += i
        else:
            odd = 1
            ans += (i - 1)
    return ans + odd

print(main(s = "abccccdd"))
print(main(s = "a"))
print(main(s = "bb"))