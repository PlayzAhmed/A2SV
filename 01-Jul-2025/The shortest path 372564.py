# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
start, end = map(int, input().split())
graph = defaultdict(list)
prev = {start: -1}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([start])

while q:
    node = q.popleft()

    if node == end: break

    for nei in graph[node]:
        if nei not in prev:
            prev[nei] = node
            q.append(nei)

if end not in prev: print(-1)
else:
    ans = []
    node = end
    while node != -1:
        ans.append(node)
        node = prev[node]

    print(len(ans) - 1)
    print(*ans[::-1])