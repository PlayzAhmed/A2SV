# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
graph = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += 1
    graph[y] += 1

if all(graph[i] == graph[1] for i in range(1, n+1)):
    print("YES")
else:
    print("NO")