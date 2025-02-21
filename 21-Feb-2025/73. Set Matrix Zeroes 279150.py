# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        rows = []
        columns = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        
        for row in rows:
            for j in range(m):
                matrix[row][j] = 0
        
        for column in columns:
            for j in range(n):
                matrix[j][column] = 0

        return matrix