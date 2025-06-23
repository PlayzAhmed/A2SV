# Problem: D - Subtree Salon: Paint ‘em All! - https://codeforces.com/gym/617023/problem/D

n = int(input())
edges = list(map(int, input().split()))
colors = list(map(int, input().split()))
moves = 1

for i in range(1, n):
    if colors[i] != colors[edges[i-1]-1]: moves += 1

print(moves)