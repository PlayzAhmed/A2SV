# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
s = sum(cards) // (n//2)

indices = defaultdict(bool)

for i in range(n):
    for j in range(i+1, n):
        if cards[i] + cards[j] == s and not indices[i] and not indices[j]:
            print(str(i+1) + " " + str(j+1))
            indices[i] = True
            indices[j] = True
