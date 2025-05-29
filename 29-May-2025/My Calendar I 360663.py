# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class Tree():
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start, end):
        cur = self

        while cur:
            if start >= cur.end:
                if not cur.right:
                    cur.right = Tree(start, end)
                    return True
                cur = cur.right
            elif end <= cur.start:
                if not cur.left:
                    cur.left = Tree(start, end)
                    return True
                cur = cur.left
            else:
                return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, startTime, endTime):
        if not self.root:
            self.root = Tree(startTime, endTime)
            return True
        return self.root.insert(startTime, endTime)