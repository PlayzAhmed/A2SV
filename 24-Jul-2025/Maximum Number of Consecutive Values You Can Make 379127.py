# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution(object):
    def getMaximumConsecutive(self, coins):
        coins.sort()
        x = 0

        for i in range(len(coins)):
            if x + 1 >= coins[i]:
                x += coins[i]
            else:
                return x + 1

        return x + 1