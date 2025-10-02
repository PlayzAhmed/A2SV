# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        dist = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
        dist[0][0] = 0
        seen = set()
        heap = []
        heappush(heap, (0, (0, 0)))

        dirr = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def valid(x, y):
            return x >= 0 and y >= 0 and x < ROWS and y < COLS

        while heap:
            cost, cur = heappop(heap)
            x, y = cur

            if cur in seen or (x == ROWS - 1 and y == COLS - 1): continue
            seen.add(cur)

            for tx, ty in dirr:
                nx, ny = x + tx, y + ty

                if valid(nx, ny):
                    eff = abs(heights[x][y] - heights[nx][ny])
                    eff = max(eff, dist[x][y])

                    if eff < dist[nx][ny]:
                        dist[nx][ny] = eff
                        heappush(heap, (eff, (nx, ny)))

        return dist[ROWS-1][COLS-1]