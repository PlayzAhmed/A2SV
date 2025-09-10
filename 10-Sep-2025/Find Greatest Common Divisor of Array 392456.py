# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution(object):
    def findGCD(self, nums):
        mn, mx = float("inf"), float("-inf")

        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)

        for x in range(mx, -1, -1):
            if mx % x == 0 and mn % x == 0:
                return x
        