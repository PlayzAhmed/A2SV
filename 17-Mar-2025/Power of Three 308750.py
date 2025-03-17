# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        return True if pow(3, ceil(log(n, 3))) == n else False
        