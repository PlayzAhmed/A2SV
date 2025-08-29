# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

n, k = map(int, input().split())
items = []
s = 0

for i in range(n):
    items.append(list(map(int, input().split())))
    s += items[i][1]

dp = [float("inf")] * (s+1)
dp[0] = 0
ans = 0

for w, v in items:
    for j in range(s, v-1, -1):
        dp[j] = min(dp[j], dp[j-v] + w)
        if dp[j] <= k:
            ans = max(ans, j)

print(ans)