# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for j in range(1, min(i, k) + 1):
        dp[i] = min(dp[i-j] + abs(h[i-j] - h[i]), dp[i])


print(dp[n-1])