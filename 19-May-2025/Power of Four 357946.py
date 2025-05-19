# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        if n < 4:
            return n == 1

        return self.isPowerOfFour(float(n)/4)