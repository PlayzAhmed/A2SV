# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        return bisect_left(nums, target)
        