# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution(object):
    def minOperations(self, nums, x):
        total = sum(nums)
        x = total - x
        n = len(nums)
        l = 0
        cur = 0
        res = float('inf')

        if x < 0:
            return -1
        
        if x == 0:
            return n

        for r in range(n):
            cur += nums[r]

            while cur > x:
                cur -= nums[l]
                l += 1

            if cur == x:
                res = min(res, n-(r - l + 1))

        return -1 if res == float('inf') else res