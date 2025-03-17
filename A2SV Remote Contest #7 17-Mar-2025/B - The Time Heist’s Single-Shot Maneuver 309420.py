# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    if n == 1:
        print("YES")
    else:
        a[0] = min(a[0], b-a[0])
        for i in range(1, n):
            t = b - a[i] 
            if t >= a[i-1]:
                if a[i] >= a[i-1]:
                    a[i] = min(a[i], t)
                else:
                    a[i] = t

        print("YES" if sorted(a) == a else "NO")