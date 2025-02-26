# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution(object):
    def construct2DArray(self, original, m, n):
        mat = [[0]*n for _ in range(m)]

        if len(original) != m * n:
            return []

        for row in range(m):
            for col in range(n):
                mat[row][col] = original[row * n + col]

        return mat
        