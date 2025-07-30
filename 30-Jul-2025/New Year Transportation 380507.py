# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, target = map(int, input().split())
a = list(map(int, input().split()))
i = 0

while i < target-1:
    i += a[i]


print("YES" if i == target-1 else "NO")