# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

counter = 0
for _ in range(int(input())):
    counter += list(map(int, input().split())).count(1)

print(counter//2)