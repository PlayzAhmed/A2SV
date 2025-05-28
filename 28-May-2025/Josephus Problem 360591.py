# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

n, k = map(int, input().split())
people = list(range(1, n + 1))

def josephus(people, k, index=0):
    if len(people) == 1:
        return people[0]
    
    index = (index + k - 1) % len(people)
    people.pop(index)
    return josephus(people, k, index)

print(josephus(people, k))