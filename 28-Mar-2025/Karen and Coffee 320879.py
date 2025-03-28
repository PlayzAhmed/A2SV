# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
recipes = []
questions = []
arr1 = [0] * 200005
arr2 = [0] * 200005
mn = float("inf")
mx = float("-inf")

for _ in range(n):
    a, b = map(int, input().split())
    recipes.append([a, b])
    mn = min(mn, a)
    mx = max(mx, b)
    arr1[a] += 1
    arr1[b+1] -= 1

for i in range(1, 200005):
    arr1[i] += arr1[i-1]
    arr2[i] += arr2[i-1] + (arr1[i] >= k)



for i in range(q):
    a, b = map(int, input().split())
    print(arr2[b]-arr2[a-1])