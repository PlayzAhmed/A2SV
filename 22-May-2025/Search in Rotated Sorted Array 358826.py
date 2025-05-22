# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        left, right, = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] < nums[mid]:
                if nums[left] == target:
                    return left
                elif nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] == target:
                    return right
                elif nums[right] > target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

