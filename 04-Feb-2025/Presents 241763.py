# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
s = input().split()
res = ""

for i in range(n):
    res += str(s.index(f'{i+1}') + 1) + " "

print(res.strip())