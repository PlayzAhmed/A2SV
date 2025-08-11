# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]

                if a - coin >= 0:
                    nextDP[a] += nextDP[a - coin]

            dp = nextDP

        return dp[amount]