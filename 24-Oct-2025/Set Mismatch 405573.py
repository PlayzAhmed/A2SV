# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        nums = Counter(nums)
        dup = 0
        mis = 0

        for i in range(1, n+1):
            if i not in nums:
                mis = i
            elif nums[i] == 2:
                dup = i


        return [dup, mis]
        