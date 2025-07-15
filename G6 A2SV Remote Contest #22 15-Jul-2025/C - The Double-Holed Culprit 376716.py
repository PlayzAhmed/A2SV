# Problem: C - The Double-Holed Culprit - https://codeforces.com/gym/622136/problem/C

from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(n):
    graph[i].append(arr[i]-1)


def search(node):
    visited = set()

    while node not in visited:
        visited.add(node)
        node = graph[node][0]

    return node+1

for i in range(n):
    arr[i] = search(i)

print(*arr)