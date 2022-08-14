"""
11. Container With Most Water
Medium

19178

1034

Add to List

Share
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
def main(height):
    """
    TIME LIMIT EXCEEDED
    res = 0
    for i in range(len(height)):
        for j in range(len(height)):
            temp = (abs(i - j)) * min(height[i], height[j])
            if temp > res:
                res = temp
    return res
    """
    left = 0
    right = len(height) - 1
    maxArea = 0
    while left < right:
        curArea = min(height[left], height[right]) * (right - left)
        if curArea > maxArea:
            maxArea = curArea
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxArea


print(main([1,8,6,2,5,4,8,3,7])) 
print(main([1, 1]))