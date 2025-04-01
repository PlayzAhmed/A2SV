# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        left = 0.0
        right = float(x)
        while left <= right:
            mid = (left + right) / 2
            sq = int(mid * mid)
            print(mid, sq)
            if sq == x:
                return int(mid)
            elif sq > x:
                right = mid
            else:
                left = mid