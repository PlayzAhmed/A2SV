# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n):
        if n == 0:
            return 0


        a, b = 0, 1

        for _ in range(n-1):
            a, b = b, a + b

        return b