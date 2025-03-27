# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]

        curSum = nums[0]
        maxSum = float("-inf")
        l = -1

        for r in range(n):
            if l == -1 and nums[r] < 0:
                l = r
            elif l > -1 and nums[r] - nums[l] < 0:
                l = r

            if l == -1 or (r == l and r == 0):
                maxSum = max(maxSum, nums[r])
            elif r == l:
                maxSum = max(maxSum, nums[r]-nums[l-1])
            else:
                maxSum = max(maxSum, nums[r]-nums[l])

        return maxSum