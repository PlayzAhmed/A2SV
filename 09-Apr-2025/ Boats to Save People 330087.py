# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution(object):
    def numRescueBoats(self, people, limit):
        p1 = 0
        p2 = len(people)-1
        res = 0
        people.sort()

        while p1 <= p2:
            if people[p1] + people[p2] <= limit:
                res += 1
                p1 += 1
                p2 -= 1
            else:
                p2 -= 1
                res += 1

        return res
        