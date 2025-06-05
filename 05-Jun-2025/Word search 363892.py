# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        n = len(word)
        row = len(board)
        col = len(board[0])
        ans = [False]
        visited = [[False] * col for _ in range(row)]

        def dfs(r, c, s="", i=0):
            if len(s) == n:
                if s == word:
                    ans[0] = True
                return

            if r < 0 or c < 0 or r >= row or c >= col or ans[0]:
                return 
            
            if board[r][c] == word[i] and not visited[r][c]:
                s += board[r][c]
                visited[r][c] = True
                dfs(r-1, c, s, i+1)
                dfs(r+1, c, s, i+1)
                dfs(r, c-1, s, i+1)
                dfs(r, c+1, s, i+1)
                visited[r][c] = False
                s = s[:-1]
            else:
                return

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and not ans[0]:
                    dfs(r, c)

        return ans[0]