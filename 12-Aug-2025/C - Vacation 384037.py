# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
dp = list(map(int, input().split()))

for _ in range(n-1):
    new = list(map(int, input().split()))
    nextDP = [0] * 3
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            nextDP[i] = max(nextDP[i], dp[j] + new[i])

    dp = nextDP

print(max(dp))