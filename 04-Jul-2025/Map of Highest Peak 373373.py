# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution(object):
    def highestPeak(self, isWater):
        ROWS = len(isWater)
        COLS = len(isWater[0])
        q = deque()
        visited = set()
        ans = [[0]*COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    q.append([i, j, 0])

        def not_valid(i, j):
            return i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited

        while q:
            i, j, h = q.popleft()

            if not_valid(i, j): continue
            if isWater[i][j] == 0: ans[i][j] = h

            visited.add((i, j))

            q.append([i + 1, j, h + 1])        
            q.append([i - 1, j, h + 1])        
            q.append([i, j + 1, h + 1])        
            q.append([i, j - 1, h + 1])

        return ans