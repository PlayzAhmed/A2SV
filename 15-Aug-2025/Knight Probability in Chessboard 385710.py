# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution(object):
    def knightProbability(self, n, k, row, col):
        memo = defaultdict(int)
        d = [
            (-2, 1),
            (-1, 2),
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
        ]

        def dfs(r, c, k):
            if k == 0:
                return 1.0

            if (r, c, k) in memo: return memo[(r, c, k)]

            count = 0.0
            for dr, dc in d:
                newr, newc = r+dr, c+dc
                
                if 0 <= newr < n and 0 <= newc < n:
                    count += dfs(newr, newc, k-1)

            memo[(r, c, k)] = count
            return memo[(r, c, k)]

        return dfs(row, col, k) / float(pow(8, k))