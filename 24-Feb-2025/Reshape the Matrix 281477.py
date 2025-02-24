# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, mat, r, c):
        rows = len(mat)
        cols = len(mat[0])

        if r*c < rows*cols or rows*cols < r*c:
            return mat

        oneD = []

        for row in range(rows):
            for col in range(cols):
                oneD.append(mat[row][col])

        res = [[0]*c for _ in range(r)]
        for row in range(r):
            for col in range(c):
                res[row][col] = oneD[row*c + col]

        return res        