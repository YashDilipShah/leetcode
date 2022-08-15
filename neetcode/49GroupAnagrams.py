"""
49. Group Anagrams
Medium

11040

352

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
def main(strs):
    main_dict = {}
    for i in strs:
        key = tuple(sorted(i))
        if key in list(main_dict.keys()):
            main_dict[key].append(i)
        else:
            main_dict[key] = [i]
    return list(main_dict.values())

print(main(["eat","tea","tan","ate","nat","bat"]))
