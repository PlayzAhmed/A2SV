# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]

        for rowI in range(n-2):
            for columnI in range(n-2):
                maxNum = 0
                for row in range(3):
                    for col in range(3):
                        maxNum = max(grid[rowI+row][columnI+col], maxNum)

                res[rowI][columnI] = maxNum

        return res


        