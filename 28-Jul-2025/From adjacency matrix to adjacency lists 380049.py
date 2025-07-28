# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

n = int(input())

for _ in range(n):
    row = list(map(int, input().split()))
    ans = []
    count = 0

    for i in range(n):
        if row[i]: ans.append(i+1); count+=1

    print(count, *ans)