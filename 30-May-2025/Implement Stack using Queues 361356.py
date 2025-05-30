# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def empty(self):
        return not self.stack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()