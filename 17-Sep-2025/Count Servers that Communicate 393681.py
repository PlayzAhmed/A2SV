# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution(object):
    def countServers(self, grid):
        rows = defaultdict(int)
        cols = defaultdict(int)
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans