# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        tot = 0

        for i in range(1, n+1):
            tot += i

        return tot - sum(nums)
        