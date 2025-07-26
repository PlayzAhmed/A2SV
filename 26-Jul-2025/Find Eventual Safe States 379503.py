# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution(object):
    def eventualSafeNodes(self, graph):
        ans = []
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = False

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = True
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)

        return ans