# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        if nums[n-1] - nums[0] == 0:
            return 0
            
        for l in range(n-1):
            if nums[l] == nums[n-1] - nums[l+1]:
                return l+1

        return -1
        