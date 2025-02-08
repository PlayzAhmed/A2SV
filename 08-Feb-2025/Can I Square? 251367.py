# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sqr = sum(a)

    side = int(math.sqrt(sqr))

    if side*side == sqr:
        print("YES")
    else:
        print("NO")
