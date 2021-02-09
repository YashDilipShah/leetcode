def nextGreaterElement(nums1, nums2):
	ans = [-1 for i in range(len(nums1))]
	for i in range(len(nums1)):
		cur_element = nums1[i]
		index_nums2 = nums2.index(cur_element)
		if max(nums2[index_nums2:]) > cur_element:
			for j in nums2[index_nums2:]:
				if j > cur_element:
					ans[i] = j
					break
	return ans

print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement([2, 4], [1, 2, 3, 4]))