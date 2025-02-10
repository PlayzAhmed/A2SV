# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n, t = map(int, input().split())
sq = t*t
z = len(str(sq))

if n == z:
    print(sq)
elif n == len(str(t)):
    print(t)
elif n > z:
    while n > z:
        sq *= 10
        z = len(str(sq))
    print(sq)
else:
    print(-1)