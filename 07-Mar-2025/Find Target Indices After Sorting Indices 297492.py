# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return res
        