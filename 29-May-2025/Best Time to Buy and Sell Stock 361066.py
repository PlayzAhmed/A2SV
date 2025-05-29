# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        prefix = [prices[0]] * n
        suffix = [prices[-1]] * n
        mx = 0

        for i in range(1, n):
            prefix[i] = min(prefix[i-1], prices[i])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i+1], prices[i])

        for i in range(n):
            mx = max(mx, abs(prefix[i] - suffix[i]))

        return mx




        