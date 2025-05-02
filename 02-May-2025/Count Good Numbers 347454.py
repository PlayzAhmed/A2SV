# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution(object):
    def countGoodNumbers(self, n):
        self.mod = pow(10, 9) + 7
        if n % 2:
            return (self.fastPow(20, n//2) * 5) % self.mod
        return self.fastPow(20, n//2) % self.mod

    def fastPow(self, x, n):
        if n == 0:
            return 1
        elif n % 2:
            return x * self.fastPow((x*x) % self.mod, (n - 1) // 2) % self.mod
        return self.fastPow((x*x) % self.mod, n // 2) % self.mod
        