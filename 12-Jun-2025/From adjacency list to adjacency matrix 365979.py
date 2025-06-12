# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
ans = [[0 for _ in range(n)] for _ in range(n)]

for r in range(n):
    edges = list(map(int, input().split()))
    if edges[0] == 0:
        continue
    else:
        for i in range(1, edges[0]+1):
            ans[r][edges[i]-1] = 1

for row in ans:
    print(*row)