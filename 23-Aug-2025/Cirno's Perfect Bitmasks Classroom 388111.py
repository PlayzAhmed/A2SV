# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    x = int(input())

    if x == 1:
        print(3)
    elif x & (x - 1):
        print(x & -x)
    else:
        print(x + 1)
