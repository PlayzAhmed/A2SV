# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution(object):
    def arrangeCoins(self, n):
        i = 0

        while n:
            if n - i - 1 >= 0:
                n -= i + 1
                i += 1
            else:
                break

        return i