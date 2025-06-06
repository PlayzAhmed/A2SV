# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x, y = i, row.index(1)
        print(abs(2 - x) + abs(2 - y))
        break