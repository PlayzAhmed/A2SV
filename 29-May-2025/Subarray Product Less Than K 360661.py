# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        p = 1
        counter = 0

        for r in range(len(nums)):
            p *= nums[r]

            while p >= k and l <= r:
                p /= nums[l]
                l += 1

            if p < k:
                counter += r - l + 1

        return counter