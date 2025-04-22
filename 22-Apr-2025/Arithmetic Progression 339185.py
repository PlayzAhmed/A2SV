# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 1:
    print(-1)
else:
    mp = defaultdict(int)
    for i in range(1, n):
        d = a[i] - a[i-1]
        mp[d] += 1

    size = len(mp)
    d = list(mp.keys())
    if size == 1 and d[0] == 0:
       print(1)
       print(a[0])
    elif size == 1 and n > 2:
        d = d[0]
        print(2)
        print(a[0] - d, a[-1] + d)
    elif size == 1 and n == 2:
        d = d[0]

        if (a[0] + a[1]) / 2 == (a[0] + a[1]) // 2:
            print(3)
            print(a[0] - d, (a[0] + a[1]) // 2, a[1] + d)
        else:
            print(2)
            print(a[0] - d, a[1] + d)
    elif size == 2:
        vals = list(mp.values())

        if (2 * min(d)) == max(d) and mp[max(d)] == 1 and mp[min(d)] >= mp[max(d)]:
            for i in range(1, n):
                if a[i] - a[i-1] == max(d):
                    print(1)
                    print(a[i] - min(d))
                    break
        else:
            print(0)
    else:
        print(0)