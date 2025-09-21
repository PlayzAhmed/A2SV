# Problem: Odd Divisor - https://codeforces.com/problemset/problem/1475/A

from math import sqrt

for _ in range(int(input())):
    n = int(input())
    f = False

    if n % 2:
        print("YES")
        continue
    while n > 1:
        n //= 2
        if n % 2 and n > 1:
            f = True
            break

    print("YES" if f else "NO")