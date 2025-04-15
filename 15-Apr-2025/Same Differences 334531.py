# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    counter = 0
    diff_dict = {}
 
    for i in range(n):
        diff = a[i] - i
        if diff in diff_dict:
            counter += diff_dict[diff]
            diff_dict[diff] += 1
        else:
            diff_dict[diff] = 1
 
    print(counter)