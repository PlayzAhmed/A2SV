# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        counting = [0]*3

        for i in nums:
            counting[i] += 1

        for i in range(len(nums)):
            if counting[0] > 0:
                nums[i] = 0
                counting[0] -= 1
            elif counting[1] > 0:
                nums[i] = 1
                counting[1] -= 1
            elif counting[2] > 0:
                nums[i] = 2
                counting[2] -= 1
        