# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                cell = board[row][col]

                if cell != ".":
                    for i in range(row+1, 9):
                        if board[i][col] == cell:
                            return False
                    
                    for i in range(col+1, 9):
                        if board[row][i] == cell:
                            return False

                if (row == 0 or row == 3 or row == 6) and (col == 0 or col == 3 or col == 6):
                    cells = []
                    for i in range(row, row+3):
                        for j in range(col, col+3):
                            if board[i][j] != ".":
                                cells.append(board[i][j])

                    if len(cells) != len(set(cells)):
                        return False


                

        return True  
        