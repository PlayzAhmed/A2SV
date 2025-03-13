# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        holder = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[holder], nums[i] = nums[i], nums[holder]
                holder += 1

        return holder
        