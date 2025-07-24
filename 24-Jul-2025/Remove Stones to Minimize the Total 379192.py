# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution(object):
    def minStoneSum(self, piles, k):
        heap = []
        s = 0

        for x in piles:
            heappush(heap, -x)
            s += x

        while k:
            x = -heappop(heap)
            diff = x // 2
            x -= diff
            s -= diff
            heappush(heap, -x)
            k -= 1

        return s

        