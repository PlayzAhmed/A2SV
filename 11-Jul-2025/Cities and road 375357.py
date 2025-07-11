# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

counter = 0
for _ in range(int(input())):
    counter += list(map(int, input().split())).count(1)

print(counter//2)