# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

from collections import defaultdict
 
for _  in range(int(input())):
    s = input()
    freq = defaultdict(int)
    c = defaultdict(int)
    n = len(s)
    l = 0
 
    if n <= 1:
        print(s[0])
        continue
 
    res = []
 
    for r in range(n):
        freq[s[r]] += 1
 
        if len(freq) > 1:
            if (r - l) % 2:
                c[s[l]] = 1
 
            freq.pop(s[l])
            l = r
    
    if freq[s[l]] % 2:
        c[s[l]] += 1
 
    for key, val in c.items():
        if val:
            res.append(key)
 
    res.sort()
 
    print("".join(res))