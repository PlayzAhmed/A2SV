# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

for _ in range(int(input())):
    l, r, d = map(int, input().split())
    if d == 1:
        print(1 if l != 1 else r+1)
        continue

    if l > d:
        print(d)
    else:
        print(d + (r - r%d))