# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])

        return res
        