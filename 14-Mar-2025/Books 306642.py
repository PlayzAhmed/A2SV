# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

i = 0 
j = 0
b = 0
res = 0

while j < n:
    if t - a[j] >= 0:
        t -= a[j]
        j += 1
        b += 1
    else:
        t += a[i]
        i += 1
        res = max(res, b)
        b -= 1

if t >= 0:
    res = max(res, b)

print(res)
