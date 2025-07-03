# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        red = defaultdict(list)
        blue = defaultdict(list)
        visited = set()
        visited.add((0, None))
        ans = [-1 for _ in range(n)]
        q = deque()
        q.append([0, 0, None])

        for p, c in redEdges:
            red[p].append(c)
        
        for p, c in blueEdges:
            blue[p].append(c)

        while q:
            node, l, color = q.popleft()
            if ans[node] == -1:
                ans[node] = l

            if color != "r":
                for nei in red[node]:
                    if (nei, "r") not in visited:
                        visited.add((nei, "r"))
                        q.append([nei, l + 1, "r"])

            if color != "b":
                for nei in blue[node]:
                    if (nei, "b") not in visited:
                        visited.add((nei, "b"))
                        q.append([nei, l + 1, "b"])

        return ans