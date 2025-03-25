# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        preSum = [[0]* (cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                preSum[r+1][c+1] = preSum[r][c+1] + preSum[r+1][c] + matrix[r][c] - preSum[r][c]

        self.matrix = preSum
        print(self.matrix)

        

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2+1][col2+1] + self.matrix[row1][col1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)