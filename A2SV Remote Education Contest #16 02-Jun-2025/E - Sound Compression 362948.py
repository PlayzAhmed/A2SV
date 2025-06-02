# Problem: E - Sound Compression - https://codeforces.com/gym/613405/problem/E

from collections import Counter
 
n, disk = map(int, input().split())
disk *= 8 
a = Counter(map(int, input().split()))
k = len(a)
a = [(key, val) for key, val in a.items()]
a.sort(key=lambda x:x[0])
max_k = pow(2, disk // n)
 
maxEnding = 0
res = 0
l = 0
 
for r in range(k):
    maxEnding += a[r][1]
    
    while r - l + 1 > max_k:
        maxEnding -= a[l][1]
        l += 1
 
    res = max(res, maxEnding)
    
 
print(n - res)