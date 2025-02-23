# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

for _ in range(int(input())):
    w = int(input())

    if w == 2 or w == 4:
        print("1")
    else:
        if w % 4 == 0:
            print(str(w//4))
        else:
            cars = w//4
            print(str(cars+((w%4)//2)))