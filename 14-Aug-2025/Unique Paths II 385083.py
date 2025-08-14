# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = [0] * (len(obstacleGrid[0]) + 1)
        dp[-2] = 1

        for i in range(len(obstacleGrid)-1, -1, -1):
            nextDP = [0] * (len(obstacleGrid[0]) + 1)

            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if not obstacleGrid[i][j]:
                    nextDP[j] = nextDP[j+1] + dp[j]

            dp = nextDP

        return dp[0]

        