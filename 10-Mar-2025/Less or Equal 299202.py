# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == n:
    print(a[-1])
    exit()

if k == 0 and a[0]-1 != 0:
    print(a[0]-1)
elif a[k-1] < a[k] and a[k-1] < 10**9:
    print(a[k-1])
else:
    print(-1)