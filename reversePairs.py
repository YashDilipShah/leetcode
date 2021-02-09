"""493. Reverse Pairs
Hard

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

    The length of the given array will not exceed 50,000.
    All the numbers in the input array are in the range of 32-bit integer.
"""
def main(nums):
    ans = 0
    def check(num, arr):
        temp = 0
        for i in arr:
            if i < num:
                temp += 1
        return temp
    for i in range(len(nums) - 1):
        ans += check(nums[i] / 2, nums[i+1:])
    return ans

print(main([1,3,2,3,1]))
print(main([2,4,3,5,1]))