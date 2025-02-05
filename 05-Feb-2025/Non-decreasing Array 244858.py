# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution(object):
    def checkPossibility(self, nums):
        num_of_mod = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                num_of_mod += 1

                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1] 

                if num_of_mod > 1:
                    return False
                
        return True