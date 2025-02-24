# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

row, col = map(int, input().split())

for r in range(row):
    if r == 0 or r == row - 1 or r % 2 == 0:
        print("#" * col, end="")
    elif r % 4 == 1:
        print("." * (col-1) + "#", end="")
    else:
        print("#" + "." * (col-1), end="")

    print()