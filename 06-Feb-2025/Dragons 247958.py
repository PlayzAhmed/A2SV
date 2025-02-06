# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())

dragons = []
die = False

for _ in range(n):
    d, b = map(int, input().split())
    if s > d:
        s += b
    else:
        dragons.append([d, b])

dragons.sort()

for d, b in dragons:
    if s > d:
        s += b
    else:
        die = True
        break

if die:
    print("NO")
else:
    print("YES")
