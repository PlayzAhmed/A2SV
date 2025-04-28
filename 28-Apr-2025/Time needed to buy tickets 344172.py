# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        i = 0
        n = len(tickets)
        res = 0

        while tickets[k] != 0:
            if tickets[i%n] != 0:
                tickets[i%n] -= 1
                res += 1
            i += 1

        return res
        