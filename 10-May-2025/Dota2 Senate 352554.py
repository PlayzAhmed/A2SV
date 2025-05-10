# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution(object):
    def predictPartyVictory(self, senate):
        r = deque()
        d = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            if r[0] < d[0]:
                i = r.popleft()
                r.append(i+n)
                d.popleft()
            else:
                i = d.popleft()
                d.append(i+n)
                r.popleft()

        return "Radiant" if r else "Dire"

        