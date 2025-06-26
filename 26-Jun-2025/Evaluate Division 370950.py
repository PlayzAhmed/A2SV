# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution(object):
    def calcEquation(self, equations, values, queries):
        result = []
        graph = defaultdict(list)

        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1/w))

        def dfs(node, target, ans, visited):
            if node == target:
                return ans

            visited.add(node)

            for nei, w in graph[node]:
                if nei not in visited:
                    res = dfs(nei, target, ans*w, visited)

                    if res != -1:
                        return res

            return -1.0

        for node, target in queries:
            if node not in graph or target not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(node, target, 1, set()))

        return result