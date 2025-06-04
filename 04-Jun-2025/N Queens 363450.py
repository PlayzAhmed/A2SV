# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        ans = []
        board = [["." for i in range(n)] for i in range(n)]
        
        def safe(board, row, col):
            for i in range(n):
                if board[row][i] == "Q":
                    return False
            
            r = row
            c = col
            while r > 0 and c > 0:
                r -= 1
                c -= 1
                if board[r][c] == "Q":
                    return False

            r = row
            c = col
            while r < n - 1 and c > 0:
                r += 1
                c -= 1
                if board[r][c] == "Q":
                    return False
            
            return True

        def backtrack(board, col=0):
            if col == n:
                flatten = []
                for row in board:
                    flatten.append("".join(row))
                ans.append(flatten)
                return

            for row in range(n):
                if safe(board, row, col):
                    board[row][col] = "Q"
                    backtrack(board, col+1)
                    board[row][col] = "."

        backtrack(board)
        
        return ans