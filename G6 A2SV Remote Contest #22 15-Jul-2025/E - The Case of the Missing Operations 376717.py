# Problem: E - The Case of the Missing Operations - https://codeforces.com/gym/622136/problem/E

from heapq import heappop, heappush

n = int(input())
heap = []
orders = []

def insert(x):
    heappush(heap, x)
    orders.append(f"insert {x}")

def removeMin():
    if not heap:
        insert(1)
    heappop(heap)
    orders.append("removeMin")

def getMin(x):
    if heap and heap[0] == x:
        orders.append(f"getMin {x}")
        return True
    return False

while n:
    op = input().split()

    if op[0] == "insert":
        insert(int(op[1]))
    elif op[0] == "removeMin":
        removeMin()
    else:
        while heap and heap[0] < int(op[1]):
            removeMin()

        if heap and heap[0] > int(op[1]) or not heap:
            insert(int(op[1]))

        getMin(int(op[1]))
            
    n -= 1

print(len(orders))
for order in orders: print(order)