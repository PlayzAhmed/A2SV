# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.canFinishEating(mid, piles) <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1


        return ans

    def canFinishEating(self, k, piles):
        h = 0
        for b in piles:
            h += ceil(float(b) / float(k))
        return h

        