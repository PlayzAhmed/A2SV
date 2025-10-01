# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = defaultdict(list)
        dist = {node:float("inf") for node in range(n)}
        dist[start_node] = -1
        heap = []
        heappush(heap, (-1, start_node))
        seen = set()

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        while heap:
            cost, node = heappop(heap)
            if node in seen: continue
            seen.add(node)
            
            for u, w in graph[node]:
                newCost = cost * w

                if newCost < dist[u]:
                    dist[u] = newCost
                    heappush(heap, (newCost, u))

        return 0 if dist[end_node] == float("inf") else -dist[end_node]