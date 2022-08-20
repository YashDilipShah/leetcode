"""
128. Longest Consecutive Sequence
Medium

12656

529

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def main(nums):
    if len(nums) > 1:
        nums = sorted(list(set(nums)))
        nums.sort()
        cur_max = 1
        cur = 1
        cur_ele = nums[0]
        for i in nums[1:]:
            if i == (cur_ele + 1):
                cur_ele = i
                cur += 1
            else:
                cur_ele = i
                cur = 1
            if cur > cur_max:
                cur_max = cur
        return cur_max
    elif len(nums) == 0:
        return 0
    else:
        return 1

print(main([100, 4, 200, 1, 3, 2]))
print(main([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
