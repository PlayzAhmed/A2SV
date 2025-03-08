# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        mn = float('inf')
        for i in range(n-k+1):
            cons = 0
            for j in range(k):
                if blocks[i+j] == "W":
                    cons += 1
            mn = min(mn, cons)
            if mn == 0:
                break

        return mn
        