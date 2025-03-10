# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def is_magic(r, c):
            row1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            row2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
            row3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            col1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            col2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
            col3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
            diagonal1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            diagonal2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]

            subgrid = [grid[r+i][c:c+3] for i in range(3)]
            subgrid = [num for row in subgrid for num in row]

            return row1 == row2 == row3 == col1 == col2 == col3 == diagonal1 == diagonal2 and sorted(subgrid) == list(range(1, 10))

        res = 0

        for row in range(rows-2):
            for col in range(cols-2):
                if is_magic(row, col):
                    res += 1
        
        return res

        