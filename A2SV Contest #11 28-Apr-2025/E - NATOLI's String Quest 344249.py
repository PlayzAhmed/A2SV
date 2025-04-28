# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

from collections import defaultdict
s = input()
alf = 'abcdefghijklmnopqrstuvwxyz}'
v = defaultdict(int)
 
c = 'z'
for ch in s:
    v[ch] += 1
    if ch < c:
        c = ch
c = ord(c) - ord('a')
 
t = []
u = []
 
for ch in s:
    while alf[c] > 'z' or (t and t[-1] <= alf[c]):
        u.append(t.pop())
    t.append(ch)
    v[ch] -= 1
    if alf[c] == ch:
        while v[alf[c]] == 0 and alf[c] <= 'z':
            c += 1
 
while t and t[-1]:
    u.append(t.pop())
print(''.join(u))