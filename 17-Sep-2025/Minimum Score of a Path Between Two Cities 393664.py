# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution(object):
    def minScore(self, n, roads):
        parent = [i for i in range(n+1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[parent[parent[x]]])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                if parentX < parentY:
                    parent[parentY] = parentX
                else:
                    parent[parentX] = parentY

        
        for a, b, _ in roads:
            union(a, b)

        p = find(1)
        ans = float("inf")

        for a, b, d in roads:
            if find(parent[a]) == p or find(parent[b]) == p:
                ans = min(ans, d)

        return ans