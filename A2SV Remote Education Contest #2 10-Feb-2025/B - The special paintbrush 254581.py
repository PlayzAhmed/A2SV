# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    

    if (s[0] == 'B' and s[-1] == 'B') or 'W' not in s:
        print(n)
    else:
        indices = []
        for i in range(len(s)):
            if s[i] == 'B':
                indices.append(i)
                
        print(indices[len(indices)-1] - indices[0] + 1)