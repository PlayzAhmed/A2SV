# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: q.append((i, j))

        def bfs():
            mins = 0
            while q:
                for _ in range(len(q)):
                    
                    r, c = q.popleft()

                    if not (r + 1 < 0 or c < 0 or r + 1 >= len(grid) or c >= len(grid[0]) or grid[r + 1][c] == 0 or grid[r + 1][c] == 2): 
                        q.append((r + 1, c))
                        grid[r + 1][c] = 2

                    if not (r - 1 < 0 or c < 0 or r - 1 >= len(grid) or c >= len(grid[0]) or grid[r - 1][c] == 0 or grid[r - 1][c] == 2): 
                        q.append((r - 1, c))
                        grid[r - 1][c] = 2

                    if not (r < 0 or c + 1 < 0 or r >= len(grid) or c + 1 >= len(grid[0]) or grid[r][c + 1] == 0 or grid[r][c + 1] == 2): 
                        q.append((r, c + 1))
                        grid[r][c + 1] = 2

                    if not (r < 0 or c - 1 < 0 or r >= len(grid) or c - 1 >= len(grid[0]) or grid[r][c - 1] == 0 or grid[r][c - 1] == 2): 
                        q.append((r, c - 1))
                        grid[r][c - 1] = 2

                if q: mins += 1

            return mins

        ans = bfs()
        return -1 if any(1 in row for row in grid) else ans