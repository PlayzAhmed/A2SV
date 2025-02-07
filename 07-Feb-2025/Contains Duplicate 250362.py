# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):

        return not (len(nums) == len(set(nums)))
        