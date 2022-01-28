"""438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
def findAnagrams(s, p):
    ans = []
    slen = len(s)
    plen = len(p)
    setp = set(p)
    chars = {}
    for i in setp:
        chars[i] = p.count(i)
    for i in range(slen - plen + 1):
        add = False
        cur_string = s[i:i + plen]
        cur_set = set(cur_string)
        if cur_set == setp:
            for j in cur_set:
                if cur_string.count(j) == chars[j]:
                    add = True
                else:
                    add = False
                    break
            if add:
                ans.append(i)
    return ans


print(findAnagrams(s= "cbaebabacd", p= "abc"))
print(findAnagrams(s= "abab", p= "ab"))