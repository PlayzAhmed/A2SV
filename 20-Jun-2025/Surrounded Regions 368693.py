# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution(object):
    def solve(self, board):
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in visited or board[i][j] == 'X': return

            visited.add((i, j))

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"

        