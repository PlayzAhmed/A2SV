# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        odd = [0] * len(graph)

        def bfs(vertex):
            if odd[vertex]: return True
            
            q = deque([vertex])
            odd[vertex] = -1

            while q:
                vertex = q.popleft()
                
                for nei in graph[vertex]:
                    if odd[vertex] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[vertex]
                
            return True
        

        for i in range(len(graph)):
            if not bfs(i): return False

        return True