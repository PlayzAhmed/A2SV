# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

n = int(input())

def geometric_sum(n):
    if n == 1:
        return 1
    return 1 * pow(1/3, n-1) + geometric_sum(n - 1)

print(geometric_sum(n))