# Problem: A - Swap to Max - https://codeforces.com/gym/622136/problem/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    for i in range(n):
        if b[i] > a[i]: a[i], b[i] = b[i], a[i]
 
    print(max(a) * max(b))