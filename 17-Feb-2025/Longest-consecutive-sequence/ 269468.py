# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        res = float('-inf')

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 1

        return max(res, count)
        