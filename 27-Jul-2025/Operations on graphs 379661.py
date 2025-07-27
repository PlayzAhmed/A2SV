# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict

graph = defaultdict(list)
n = int(input())
k = int(input())

for _ in range(k):
    op = input().split()

    if op[0] == "1":
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    elif op[0] == "2":
        if graph[op[1]]:
            print(*graph[op[1]])