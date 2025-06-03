# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution(object):
    def maxScore(self, cardPoints, k):
        minEnd = 0
        res = float('inf')
        n = len(cardPoints)
        l = 0

        for r in range(n):
            minEnd += cardPoints[r]

            while r - l + 1 > n - k:
                minEnd -= cardPoints[l]
                l += 1

            if r - l + 1 == n - k:
                res = min(res, minEnd)

        return sum(cardPoints) - res
        