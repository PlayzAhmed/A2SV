# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
a = list(map(int, input().split()))
s, d = 0, 0
p1 = 0
p2 = n - 1

while p1 <= p2:
    if a[p1] > a[p2]:
        s += a[p1]
        p1 += 1
    else:
        s += a[p2]
        p2 -= 1

    if p1 <= p2:
        if a[p1] > a[p2]:
            d += a[p1]
            p1 += 1
        else:
            d += a[p2]
            p2 -= 1

print(s, d)