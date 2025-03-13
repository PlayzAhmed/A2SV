# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

import sys


def check_1100(buf, i, n):
    if i < 0 or i >= n - 3:
        return False
    return buf[i] == '1' and buf[i + 1] == '1' and buf[i + 2] == '0' and buf[i + 3] == '0'


def solve():
    buf = list(sys.stdin.readline().strip())
    n = len(buf)
    count = sum(1 for i in range(n) if check_1100(buf, i, n))

    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        i, v = map(int, sys.stdin.readline().split())
        i -= 1
        if buf[i] != str(v):
            before = False
            for j in range(i - 3, i + 1):
                before |= check_1100(buf, j, n)

            buf[i] = str(v)
            after = False
            for j in range(i - 3, i + 1):
                after |= check_1100(buf, j, n)

            count += after - before
        print("YES" if count else "NO")


t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()