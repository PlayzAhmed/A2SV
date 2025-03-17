# Problem: E - Quantum Severance – A Battle of Edges - https://codeforces.com/gym/596004/problem/E

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0] * n
    prefix[-1] = a[-1] * -1 if a[-1] < 0 else 0

    for i in range(n-2, -1, -1):
        if a[i] < 0:
            prefix[i] = prefix[i+1] + (a[i] * -1)
        else:
            prefix[i] = prefix[i+1]

    res = 0
    s = 0

    for i in range(n):
        if a[i] > 0:
            s += a[i]
        
        res = max(res, s+prefix[i])

    print(res)