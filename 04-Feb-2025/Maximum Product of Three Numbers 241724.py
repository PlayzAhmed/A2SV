# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        p1 = nums[-1] * nums[-2] * nums[-3]
        p2 = nums[0] * nums[1] * nums[-1]

        return max(p1, p2)
        