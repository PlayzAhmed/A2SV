# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution(object):
    def shortestBridge(self, grid):
        n = len(grid)
        
        first_island = set()
        visited = set()
        dq = deque()
        ans = float('inf')
        
        def valid_cell(i, j):
            return not (i >= n or j >= n or i < 0 or j < 0)
        
        def find_island(i, j):
            q = deque([(i, j)])
            
            while q:
                i, j = q.popleft()
                
                if not valid_cell(i, j):
                    continue

                if (i, j) in first_island or grid[i][j] == 0:
                    continue
                
                first_island.add((i, j))
                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i, j+1))
                q.append((i, j-1))
                
                if (valid_cell(i+1, j) and grid[i+1][j] == 0) or (valid_cell(i-1, j) and grid[i-1][j] == 0) or (valid_cell(i, j+1) and grid[i][j+1] == 0) or (valid_cell(i, j-1) and grid[i][j-1] == 0):
                    dq.append((i, j, -1))
                    
        for i in range(n):
            flag = False
            for j in range(n):
                if grid[i][j] == 1:
                    find_island(i, j)
                    flag = True
                    break
            if flag: break
                
        while dq:
            i, j, path = dq.popleft()
            
            if ((i, j) in first_island and path != -1) or (i, j) in visited or not valid_cell(i, j):
                continue
                
            if grid[i][j] == 1 and (i, j) not in first_island:
                ans = min(ans, path)
                continue
            
            visited.add((i, j))
            
            dq.append((i+1, j, path+1))
            dq.append((i-1, j, path+1))
            dq.append((i, j+1, path+1))
            dq.append((i, j-1, path+1))
            
        return ans
        