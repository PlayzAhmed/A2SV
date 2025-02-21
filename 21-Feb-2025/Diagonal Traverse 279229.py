# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
        maxR = len(mat)
        maxC = len(mat[0])
        row = 0
        col = 0
        upwards = True
        res = []

        while row < maxR and col < maxC and len(res) < maxR*maxC:
            res.append(mat[row][col])
            if upwards:
                if row-1 >= 0 and col+1 < maxC:
                    row -= 1
                    col += 1
                else:
                    upwards = False
                    if col+1 < maxC:
                        col += 1
                    elif row+1 < maxR:
                        row += 1
            else:
                if row+1 < maxR and col - 1 >= 0:
                    row += 1
                    col -= 1
                else:
                    upwards = True
                    if row+1 < maxR:
                        row += 1
                    elif col+1 < maxC:
                        col += 1

        return res