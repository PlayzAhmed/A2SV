# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(1, n-1, 2):
            if i + 1 < n:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums
        