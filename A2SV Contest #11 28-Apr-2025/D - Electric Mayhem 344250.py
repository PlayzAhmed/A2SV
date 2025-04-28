# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s = input()
stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

print("No" if stack else "Yes")