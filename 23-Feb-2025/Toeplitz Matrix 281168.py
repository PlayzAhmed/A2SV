# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False

        return True
        