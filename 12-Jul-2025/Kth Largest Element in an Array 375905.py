# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution(object):
    def findKthLargest(self, nums, k):
        return nlargest(k, nums)[-1]

        