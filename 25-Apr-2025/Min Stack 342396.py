# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if (self.min and self.min[-1] >= val) or not self.min:
            self.min.append(val)
        

    def pop(self):
        x = self.stack.pop()
        if self.min and self.min[-1] == x:
            self.min.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()