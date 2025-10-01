# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        graph = defaultdict(list)
        heap = []
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        for i in range(n):
            heappush(heap, (self.findPaths(n, graph, distanceThreshold, i), -i))

        return -heappop(heap)[1]

    def findPaths(self, n, graph, k, start):
        dist = {node:float("inf") for node in range(n)}
        dist[start] = 0 
        heap = []
        heappush(heap, (0, start))
        seen = set()
        ans = 0

        while heap:
            distance, node = heappop(heap)

            if node in seen: continue
            
            seen.add(node)

            for child, cost in graph[node]:
                newDistance = cost + distance

                if newDistance < dist[child] and newDistance <= k:
                    dist[child] = newDistance
                    heappush(heap, (newDistance, child))

        dist[start] = k+1

        for val in dist.values():
            if val <= k:
                ans += 1

        return ans