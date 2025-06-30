# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

n, k = map(int, input().split())

for _ in range(k):
    n = n - 1 if n % 10 else n // 10

print(n)