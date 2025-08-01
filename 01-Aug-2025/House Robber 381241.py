# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        x, y = 0, 0

        for n in nums:
            temp = max(x+n, y)
            x = y
            y = temp

        return y
        