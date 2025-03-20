# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = -1
        right = 0
        n = len(nums)
        prefix = [nums[0]]
        mn = float('inf')
        
        if target in nums:
            return 1

        for i in range(1, n):
            prefix.append(nums[i] + prefix[i-1]) 

        if prefix[-1] < target:
            return 0

        while left < right and right < n:
            if left == -1:
                if prefix[right] >= target:
                    mn = min(right+1, mn)
                    left += 1
                else:
                    right += 1
            elif left > -1:
                if prefix[right] - prefix[left] >= target:
                    left += 1
                    mn = min(right-left+1, mn)
                else:
                    right += 1

        return mn

        