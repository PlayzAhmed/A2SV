# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)/2

            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid
        
        return -1
        