# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution(object):
    def openLock(self, deadends, target):
        q = deque()
        q.append(["0000", 0])
        visited = set()
        deadends = set(deadends)
        mp = {
            "0": ["1", "9"],
            "1": ["2", "0"],
            "2": ["3", "1"],
            "3": ["4", "2"],
            "4": ["5", "3"],
            "5": ["6", "4"],
            "6": ["7", "5"],
            "7": ["8", "6"],
            "8": ["9", "7"],
            "9": ["0", "8"]
        }

        while q:
            lock, length = q.popleft()
            if lock == target: return length
            if lock in deadends or lock in visited: continue

            visited.add(lock)

            for i in range(len(lock)):
                q.append([lock[:i] + mp[lock[i]][0] + lock[i+1:], length+1])
                q.append([lock[:i] + mp[lock[i]][1] + lock[i+1:], length+1])

        return -1