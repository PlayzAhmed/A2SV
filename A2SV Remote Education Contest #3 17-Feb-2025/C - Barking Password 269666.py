# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input()
first = False
second = False

for _ in range(int(input())):
    s = input()

    if password == s:
        print("YES")
        exit()

    if password[0] == s[1]:
        first = True

    if password[1] == s[0]:
        second = True

    if first and second:
        break

if first and second:
    print("YES")
else:
    print("NO")