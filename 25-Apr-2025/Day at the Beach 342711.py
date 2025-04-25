# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

n = int(input())
h = list(map(int, input().split()))

premax = [0] * n
sufmin = [0] * n

premax[0] = h[0]
for i in range(1, n):
    premax[i] = max(premax[i - 1], h[i])

sufmin[-1] = h[-1]
for i in range(n - 2, -1, -1):
    sufmin[i] = min(sufmin[i + 1], h[i])

res = 0
for i in range(n - 1):
    if premax[i] <= sufmin[i + 1]:
        res += 1

print(res + 1)