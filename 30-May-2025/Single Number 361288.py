# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        nums = Counter(nums)
        
        for key, val in nums.items():
            if val == 1:
                return key