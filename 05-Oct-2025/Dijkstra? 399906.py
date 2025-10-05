# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

from collections import defaultdict
from heapq import heappop, heappush
 
n, m = map(int, input().split())
graph = defaultdict(list)
 
for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
 
 
def bfs(n):
    heap = []
    dist = {node:float("inf") for node in range(1, n+1)}
    dist[1] = 0
    parent = {1:None}
    seen = set()
    heappush(heap, (0, 1))
 
    while heap:
        cost, node = heappop(heap)
 
        if node == n: 
            path = []
            while node is not None:
                path.append(str(node))
                node = parent[node]

            return " ".join(reversed(path))
        
        if node in seen: continue
 
        seen.add(node)
 
        for child, w in graph[node]:
            newCost = cost + w
            if newCost < dist[child]:
                dist[child] = newCost
                parent[child] = node
                heappush(heap, (newCost, child))
 
    return -1
 
print(bfs(n))