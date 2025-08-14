# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution(object):
    def minFallingPathSum(self, matrix):
        dp = matrix[0] + []

        for i in range(1, len(matrix)):
            nextDP = [float('inf')] * len(matrix)

            for j in range(len(matrix)):
                for k in range(-1, 2):
                    if len(matrix) > j + k >= 0:
                        nextDP[j] = min(nextDP[j], dp[j+k]+matrix[i][j])

            dp = nextDP

        return min(dp)
                

        