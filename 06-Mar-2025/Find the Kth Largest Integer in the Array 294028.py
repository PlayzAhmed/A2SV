# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution(object):
    def kthLargestNumber(self, nums, m):
        return sorted(nums, key=lambda x: int(x))[len(nums)-m]
        