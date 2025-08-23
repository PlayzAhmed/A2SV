# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        cache = defaultdict(int)

        def dps(i=0, state=True):
            if i >= len(prices):
                return 0
            
            if (i, state) in cache:
                return cache[i, state]

            if state:
                cache[i, state] = max(
                    dps(i+1, False) - prices[i], 
                    dps(i+1, True)
                    )
            else:
                cache[i, state] = max(
                    dps(i+2, True) + prices[i], 
                    dps(i+1, False)
                    )
           
            return cache[i, state]

        return dps()