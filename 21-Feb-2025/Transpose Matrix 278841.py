# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        transpose = [[0]*rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                transpose[j][i] = matrix[i][j]

        return transpose
        