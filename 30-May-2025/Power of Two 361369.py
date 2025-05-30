# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0: return False
        if n == 1: return True
        return n == pow(2, int(log(n, 2)))
        