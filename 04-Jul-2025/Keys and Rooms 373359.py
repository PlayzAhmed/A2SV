# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()
        q = deque([0])

        while q:
            i = q.popleft()

            if i in visited: continue

            visited.add(i)

            for key in rooms[i]:
                q.append(key)

        return len(visited) == len(rooms)
        