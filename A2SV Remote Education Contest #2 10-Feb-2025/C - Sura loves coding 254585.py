# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
s = input()
res = [" "]*n
j = 0
k = n-1

if n % 2 == 1:
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            res[k] = s[i]
            k -= 1
        else:
            res[j] = s[i]
            j += 1
else:
    for i in range(n-1, -1, -1):
        if i % 2 == 1:
            res[k] = s[i]
            k -= 1
        else:
            res[j] = s[i]
            j += 1

print("".join(res))