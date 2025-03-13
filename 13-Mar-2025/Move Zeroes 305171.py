# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        holder = 0

        for i in range(n):
            if nums[i] != 0:
                nums[holder], nums[i] = nums[i], nums[holder]
                holder += 1

        return nums
        