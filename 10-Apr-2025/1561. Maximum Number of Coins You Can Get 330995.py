# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        piles = piles[n//3:]

        s = 0

        for i in range(0, n-(n//3), 2):
            s += piles[i]

        return s