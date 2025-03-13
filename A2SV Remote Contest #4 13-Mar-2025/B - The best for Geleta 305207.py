# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res, mx = [0]*m, max(a)
    
    for i in range(m):
        op, left, right = map(str, input().split())
        left = int(left)
        right = int(right)

        if left <= mx <= right:
            if op == '+':
                mx += 1
                res[i] = mx
            else:
                mx -= 1
                res[i] = mx
            
            continue
        
        res[i] = mx
        
    print(*res)