# Problem: B - Lifeboat Lineup - https://codeforces.com/gym/622136/problem/B

import heapq

n = int(input())
heap = []
mp = {
    "rat": 0,
    "woman": 1,
    "child": 1,
    "man": 2,
    "captain": 3
}

for i in range(n):
    name, role = input().split()
    heapq.heappush(heap, (mp[role], i, name))


while heap:
    _, _, name = heapq.heappop(heap)
    print(name)