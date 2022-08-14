"""
FAILED
3. Longest Substring Without Repeating Characters
Medium

27438

1180

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
def main(s):
    if len(list(s)) == len(set(s)):
        return len(s)
    elif len(s) > 0:
        def ss(index, string):
            cur_str = string[index]
            cur_index = index
            #print("Started here")
            while len(list(cur_str)) == len(set(cur_str)):
                #print(cur_str)
                try:
                    cur_str += string[cur_index + 1]
                    cur_index += 1
                except:
                    break
            return len(cur_str) - 1
        ans = -1
        for i in range(len(s)):
            temp = ss(i, s)
            if temp > ans:
                ans = temp
        return ans
    else:
        return 0
print(main("abcabcbb"))
print(main("bbbbb"))
print(main("pwwkew"))

def solution(s):
    max_len = 0
    cur_string = ""
    for char in s:
        if char not in cur_string:
            cur_string += char
        else:
            for i in range(len(cur_string)):
                if cur_string[i] == char:
                    cur_string = cur_string[i+1:]+char
                    break
        if len(cur_string)>max_len:
            max_len = len(cur_string)
    return max_len