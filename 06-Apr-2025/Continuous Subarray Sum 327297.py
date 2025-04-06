# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder = {0: -1}
        t = 0
        
        for i in range(len(nums)):
            t += nums[i]
            r = t % k 

            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False