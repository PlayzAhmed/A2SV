# Problem: C - Happy Partitioning - https://codeforces.com/gym/590201/problem/C

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip()))

    prefix_zeros = [0] * (n + 1)
    suffix_ones = [0] * (n + 1)

    for i in range(n):
        prefix_zeros[i + 1] = prefix_zeros[i] + (a[i] == 0)

    for i in range(n - 1, -1, -1):
        suffix_ones[i] = suffix_ones[i + 1] + (a[i] == 1)

    best_pos = -1
    best_dist = float('inf')

    for i in range(n + 1): 
        left_zeros = prefix_zeros[i]
        left_len = i
        right_ones = suffix_ones[i]
        right_len = n - i

        if left_zeros >= left_len / 2 and right_ones >= right_len / 2:
            dist = abs(n - 2 * i)
            if dist < best_dist:
                best_dist = dist
                best_pos = i

    if best_pos != -1:
        print(best_pos)
    else:
        if a.count(0) > n / 2:
            print(n)
        else:
            print(0)
