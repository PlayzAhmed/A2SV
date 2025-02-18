# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
messages = []

for _ in range(n):
    s = input()
    messages.append(s)

messages = messages[::-1]

his = {}

for m in messages:
    if m not in his:
        print(m)
        his[m] = 1