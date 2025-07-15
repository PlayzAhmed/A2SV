# Problem: D - Split the Difference! - https://codeforces.com/gym/622136/problem/D

n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == k:
    print(0)
elif n == 1:
    print(a[-1] - a[0])
else:
    gaps = [0] * (n-1)
    ans = a[-1] - a[0]

    for i in range(n-1):
        gaps[i] = a[i+1] - a[i]
        
    gaps.sort(reverse=True)
    
    for i in range(k-1):
        ans -= gaps[i]

    print(ans)