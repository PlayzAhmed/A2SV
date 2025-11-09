# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = True

    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            flag = False
            break

    print("YES" if flag else "NO")