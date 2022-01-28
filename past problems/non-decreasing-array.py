def checkPossibility(nums):
    count = 0
    for i in range(1, len(nums)):
        if max(nums[:i]) > nums[i]:
            count += 1
    return count < 2

print(checkPossibility([4, 2, 3]))