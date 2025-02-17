# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        matrix = []
        for m in range(n):
            matrix.append([0]*n)
        ecol = 0
        erow = 0
        ocol = (((n*n)//2) % n)
        orow = ((n*n)//2) // n

        for i in range(1, n*n + 1):
            if i % 2 == 0:
                matrix[erow][ecol] = i
                if erow + 1 < n and ecol+1 == n:
                    erow += 1
                    ecol = 0
                else:
                    ecol += 1
            else:
                matrix[orow][ocol] = i
                if orow + 1 < n and ocol + 1 == n:
                    orow += 1
                    ocol = 0
                else:
                    ocol += 1
        
        for row in matrix:
            print(*row)
