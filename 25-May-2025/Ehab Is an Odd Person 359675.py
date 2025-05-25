# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
 
e = 0
o = 0
 
for x in a:
    if x % 2:
        o = 1
    else:
        e = 1
 
    if e and o:
        a.sort()
        break
 
print(*a)