# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = []

for _ in range(n):
    m, f = map(int, input().split())
    friends.append((m, f))

friends.sort(key=lambda x: x[0])

l = 0 
mx = friends[0][1]
res = friends[0][1]

for r in range(1, n):
    while friends[r][0] - friends[l][0] >= d:
        mx -= friends[l][1]
        l += 1
        
    mx += friends[r][1]
    res = max(mx, res)


print(res)