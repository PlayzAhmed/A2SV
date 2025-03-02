# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution(object):
    def maxMatrixSum(self, matrix):
        n = len(matrix)
        negatives = 0
        smallest = float('inf')
        s = 0

        for row in range(n):
            for col in range(n):
                num = matrix[row][col]
                s += abs(num)
                smallest = min(smallest, abs(num))
                if num < 0:
                    negatives += 1


        if negatives % 2 == 0:
            return s
        else:
            return s - (smallest*2)
        