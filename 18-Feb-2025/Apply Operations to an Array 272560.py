# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        res = [0]*n
        idx = 0
        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1] and nums[i] > 0:
                res[idx] = nums[i]*2
                idx += 1
                nums[i+1] = 0
            elif nums[i] > 0:
                res[idx] = nums[i]
                idx += 1

        return res