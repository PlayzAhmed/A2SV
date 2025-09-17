# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        nums = Counter(nums)
        res = []
        for num, freq in nums.items():
            if freq == 2:
                res.append(num)

        return res
        