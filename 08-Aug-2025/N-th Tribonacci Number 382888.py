# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution(object):
    def tribonacci(self, n):
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        
        return dp[n]