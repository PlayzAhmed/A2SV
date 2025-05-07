# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            left = nums[mid-1] if mid - 1 >= 0 else float('-inf')
            right = nums[mid+1] if mid + 1 < n else float('-inf')

            if left < nums[mid] > right:
                return mid
            elif nums[mid] < right:
                low = mid + 1
            else:
                high = mid        