# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost) + 1)
        dp[-2] = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])