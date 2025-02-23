# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            left = 0
            right = cols-1
            

            if target < matrix[row][left] or target > matrix[row][right]:
                continue

            while left <= right:
                mid = (left+right)//2
                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    left = mid+1
                elif target < matrix[row][mid]:
                    right = mid-1

        return False