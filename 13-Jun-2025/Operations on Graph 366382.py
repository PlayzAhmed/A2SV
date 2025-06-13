# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)

for _ in range(k):
    op = list(map(int, input().split()))
    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    elif op[1] in graph:
        print(*graph[op[1]])