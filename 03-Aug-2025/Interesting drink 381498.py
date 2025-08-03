# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())

for _ in range(q):
    x = int(input())
    l, r = 0, n-1

    while l <= r:
        mid = (l+r) // 2

        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    
    print(l)