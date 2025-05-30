# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
        

    def pop(self):
        return self.queue.pop(0)
        

    def peek(self):
        return self.queue[0]
        

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()