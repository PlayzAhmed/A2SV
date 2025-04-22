# Problem: A - How i met your mother - Last Forever - https://codeforces.com/gym/604857/problem/A

from collections import Counter
 
n = int(input())
a = Counter(input())
ones = [1] * a["n"]
zeros = [0] * a["z"]
 
res = ones + zeros
 
print(*res)