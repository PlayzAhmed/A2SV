# Problem: Twin Permutations - https://codeforces.com/problemset/problem/1831/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []

    for x in a:
        res.append(n-x+1)

    print(*res)