# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

n = int(input())
a = list(map(int, input().split()))

if a[-1] >= n:
    print(1)
    exit()

diff = [0] * (n + 1)

for i in range(1, n):
    if a[i] > 0:
        left = max(0, i - a[i])
        diff[left] += 1 
        diff[i] -= 1

kills = 0
current = 0
for i in range(n):
    current += diff[i]
    if current > 0:
        kills += 1

print(n - kills)
