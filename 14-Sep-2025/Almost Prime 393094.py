# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

from math import sqrt

n = int(input())
ans = 0
primes = []

def isPrime(x):
    if x < 2: return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    primes.append(x)
    return True

def isAlmostPrime(x):
    c = 0
    for y in primes:
        if x % y == 0:
            c += 1

    return c == 2

for i in range(2, n+1):
    isPrime(i)
    if isAlmostPrime(i):
        ans += 1

print(ans)