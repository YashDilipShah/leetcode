"""594. Longest Harmonious Subsequence
Easy

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

 

Note: The length of the input array will not exceed 20,000.
"""

def findLHS(nums):
    from collections import Counter
    ans = -1
    dict = Counter(nums)
    nums = set(nums)
    for i in nums:
        if (i+1) in dict.keys():
            if dict[i] + dict[i+1] > ans:
                ans = dict[i] + dict[i+1]
    return ans

print(findLHS([1,3,2,2,5,2,3,7]))