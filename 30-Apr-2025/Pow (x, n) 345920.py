# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            n *= -1
            x = 1 / x

        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.myPow(x*x, n/2)

        return x * self.myPow(x*x, (n-1)/2)

        