# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution(object):
    def findSafeWalk(self, grid, health):
        heap = []
        dist = {(x, y):float("inf") for x in range(len(grid)) for y in range(len(grid[0]))}
        dist[(0, 0)] = grid[0][0]
        seen = set()
        dirr = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]

        heappush(heap, (grid[0][0], (0, 0)))

        def valid(x, y):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

        while heap:
            cost, cur = heappop(heap)
            x, y = cur
            
            if x == len(grid)-1 and y == len(grid[0])-1:
                return True

            if cur in seen:
                continue

            seen.add(cur)

            for dx, dy in dirr:
                nx, ny = x+dx, y+dy
                if not valid(nx, ny): continue
                newCost = cost + grid[nx][ny]
                if newCost < dist[(nx, ny)] and newCost < health:
                    dist[(nx, ny)] = newCost
                    heappush(heap, (newCost, (nx, ny)))

        return False