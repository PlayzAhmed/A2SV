# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        dp = [poured]

        for i in range(1, query_row+1):
            cur = [0] * (i+1)

            for j in range(len(dp)):
                add = max(float(dp[j]-1) * 0.5, 0)
                cur[j] += add
                cur[j+1] += add

            dp = cur

        return min(dp[query_glass], 1.0)
