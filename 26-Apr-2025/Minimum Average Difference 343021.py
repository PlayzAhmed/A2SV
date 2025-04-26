# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution(object):
    def minimumAverageDifference(self, nums):
        res = float('inf')
        index = -1
        n = len(nums)
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        for i in range(n):
            last = ((nums[-1] - nums[i]) // (n-i-1)) if n - i - 1 > 0 else 0
            avg = abs((nums[i] // (i+1)) - last)
            if avg < res:
                res = avg
                index = i

        return index
        