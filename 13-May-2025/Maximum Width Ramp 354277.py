# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        res = 0
        pre = [nums[-1]] * n
        l = 0

        for i in range(n-2, -1, -1):
            pre[i] = max(pre[i+1], nums[i])

        for r in range(n):
            if nums[l] <= pre[r]:
                res = max(r-l, res)

            while nums[l] > pre[r] and l <= r:
                l += 1


        return res