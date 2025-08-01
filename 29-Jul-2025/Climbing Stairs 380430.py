# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        memo = {1:1, 2:2}

        def climb(n):
            if n not in memo:
                memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        
        return climb(n)