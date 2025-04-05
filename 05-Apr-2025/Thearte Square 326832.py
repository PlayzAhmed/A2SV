# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

n, m, a = map(int, input().split())

res = 0

if n % a == 0:
    res += n // a
else:
    res += n // a + 1

if m % a == 0:
    res *= m // a
else:
    res *= m // a + 1

print(res)