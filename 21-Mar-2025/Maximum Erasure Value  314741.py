# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        mx = 0
        s = 0
        freq = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            freq[nums[r]] += 1
            s += nums[r]
            while freq[nums[r]] > 1:
                freq[nums[l]] -= 1
                s -= nums[l]
                l += 1
                
            mx = max(mx, s)


        return mx
                

