# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        res = [-1] * n
        l = -1
        for i in range(2*k, n):
            if l == -1:
                res[i-k] = nums[i] // (2 * k + 1)
                l += 1
            else:
                res[i-k] = (nums[i] - nums[l]) // (2 * k + 1)
                l += 1

        return res