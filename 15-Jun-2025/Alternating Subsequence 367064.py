# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxp, maxn = float('-inf'), float('-inf')
    arrp, arrn = [0, 0], [0, 0]
    signp, signn = True, True

    for r in range(n):
        if signp and a[r] > 0:
            maxp = max(maxp, a[r])
            if r+1 < n and a[r+1] < 0:
                signp = False
                arrp[0] += maxp
                arrp[1] += 1
                maxp = float('-inf')
        elif not signp and a[r] < 0:
            maxp = max(maxp, a[r])
            if r+1 < n and a[r+1] > 0:
                signp = True
                arrp[0] += maxp
                arrp[1] += 1
                maxp = float('-inf')

        if signn and a[r] < 0:
            maxn = max(maxn, a[r])
            if r+1 < n and a[r+1] > 0:
                signn = False
                arrn[0] += maxn
                arrn[1] += 1
                maxn = float('-inf')
        elif not signn and a[r] > 0:
            maxn = max(maxn, a[r])
            if r+1 < n and a[r+1] < 0:
                signn = True
                arrn[0] += maxn
                arrn[1] += 1
                maxn = float('-inf')

    if maxp != float('-inf'):
        arrp[0] += maxp
        arrp[1] += 1
    if maxn != float('-inf'):
        arrn[0] += maxn
        arrn[1] += 1

    if arrp[1] == arrn[1]:
        print(max(arrp[0], arrn[0]))
    else:
        print(arrp[0] if arrp[1] > arrn[1] else arrn[0])