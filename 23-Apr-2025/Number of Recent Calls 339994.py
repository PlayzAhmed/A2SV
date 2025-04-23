# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter(object):

    def __init__(self):
        self.queue = []
        self.left = 0

    def ping(self, t):
        self.queue.append(t)

        while self.queue[self.left] < t - 3000:
            self.left += 1

        return len(self.queue) - self.left
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)