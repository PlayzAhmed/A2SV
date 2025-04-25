# Problem: Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        p = 1
        visited = True

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and visited:
                visited = False
                nums[p] = nums[i]
                p += 1
            elif nums[i] != nums[i-1]:
                nums[p] = nums[i]
                visited = True
                p += 1

        return p
        