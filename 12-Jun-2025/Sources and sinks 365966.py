# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

n = int(input())
graph = []
ans = [[], []]

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def check(node):
    global n
    sink = True
    source = True
    for r in range(n):
        if graph[r][node] == 1: 
            source = False
            break
    
    for c in range(n):
        if graph[node][c] == 1:
            sink = False
            break

    return source, sink

for x in range(n):
    source, sink = check(x)
    if source:
        ans[0].append(x+1)
    if sink:
        ans[1].append(x+1)

print(len(ans[0]), *ans[0])
print(len(ans[1]), *ans[1])