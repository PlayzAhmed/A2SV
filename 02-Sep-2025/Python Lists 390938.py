# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    myList = []
    
    for _ in range(N):
        op = input().split()

        if op[0] == "insert":
            myList.insert(int(op[1]), int(op[2]))
        elif op[0] == "print":
            print(myList)
        elif op[0] == "remove":
            myList.remove(int(op[1]))
        elif op[0] == "append":
            myList.append(int(op[1]))
        elif op[0] == "sort":
            myList.sort()
        elif op[0] == "pop":
            myList.pop()
        else:
            myList.reverse()
