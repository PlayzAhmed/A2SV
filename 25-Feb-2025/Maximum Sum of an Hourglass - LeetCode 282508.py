# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution(object):
    def maxSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        preSum = [[0]*(cols+1) for _ in range(rows+1)]
        maxSum = -1


        for row in range(1, rows+1): 
            for col in range(1, cols+1):
                preSum[row][col] = grid[row-1][col-1] + preSum[row-1][col] + preSum[row][col-1] - preSum[row-1][col-1]

        for row in range(rows-2):
            for col in range(cols-2):
                subMatrix = preSum[row+3][col+3] - preSum[row][col+3] - preSum[row+3][col] + preSum[row][col]
                hourglass = subMatrix - grid[row+1][col] - grid[row+1][col+2]
                maxSum = max(maxSum, hourglass)

        return maxSum