# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j+1)

for i in range(n):
    if graph[i]:
        print(len(graph[i]), *graph[i])
    else:
        print(0)
