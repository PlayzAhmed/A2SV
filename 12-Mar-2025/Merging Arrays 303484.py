# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i = 0
j = 0

while i < n and j < m:
    if a[i] > b[j]:
        res.append(b[j])
        j += 1
    else:
        res.append(a[i])
        i += 1

if i == n:
    res.extend(b[j:])
else:
    res.extend(a[i:])

res = list(map(str, res))
print(" ".join(res))