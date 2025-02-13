# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        nums = Counter(nums)
        res = []

        for val, count in nums.items():
            if count == 2:
                res.append(val)

        return res
            