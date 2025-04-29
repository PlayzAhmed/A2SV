# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n < 4:
            return False

        return self.isPowerOfFour(float(n)/4)
        