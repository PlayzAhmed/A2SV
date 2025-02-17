# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

for _ in range(int(input())):
    n, k = map(int, input().split())
    health = list(map(int, input().split()))
    position = list(map(int, input().split()))
    zombies = []
    r, idx, kills = 0, 0, 0
    die = False
    for i in range(len(health)):
        zombies.append([abs(position[i]), health[i]])

    zombies.sort()
    bullet = k
    while not die and kills < n and idx < n:
        if bullet == 0:
            r += 1
            bullet += k

        if zombies[idx][0] - r > 0:
            if bullet >= zombies[idx][1]:
                bullet = bullet - zombies[idx][1]
                kills += 1
                idx += 1
            else:
                zombies[idx][1] -= bullet
                bullet = 0
        else:
            die = True
    

    print("NO") if die else print("YES")