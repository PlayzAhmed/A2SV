# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import defaultdict, deque

n, m = map(int, input().split())
train = defaultdict(set)
bus = defaultdict(set)

for _ in range(m):
    u, v = map(int, input().split())

    train[u].add(v)
    train[v].add(u)

for parent in range(1, n+1):
    for child in range(parent+1, n+1):
        if child not in train[parent]:
            bus[parent].add(child)
            bus[child].add(parent)

def bfs(t):
    ans = []
    seen = set()
    q = deque([(1, [1])])

    while q:
        node, path = q.popleft()
        
        if node == n:
            ans.append(path)
            continue

        if node in seen:
            continue

        seen.add(node)

        for x in train[node] if t else bus[node]:
            if x not in seen:
                q.append((x, path+[x]))
    return ans

trainRoutes = bfs(True)
busRoutes = bfs(False)

def ans():
    if not trainRoutes or not busRoutes:
        return -1
    
    ans = float("inf")

    for busRoute in busRoutes:
        for trainRoute in trainRoutes:
            f = True
            for i in range(1, min(len(trainRoute), len(busRoute)) - 1):
                if trainRoute[i] == busRoute[i]:
                    f = False
                    break

            if f:
                ans = min(ans, max(len(busRoute), len(trainRoute)) - 1)

    return ans

print(ans())