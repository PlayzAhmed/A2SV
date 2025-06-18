# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        visited = set()

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(vertex):
            if vertex == destination:
                return True

            flag = False

            for i in graph[vertex]:
                if i not in visited:
                    visited.add(i)
                    flag = flag or dfs(i)

            return flag

        return dfs(source)