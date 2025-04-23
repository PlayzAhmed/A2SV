# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream(object):

    def __init__(self, value, k):
        self.queue = []
        self.value = value
        self.size = k
        self.left = -k+1
        self.unwanted = 0
        

    def consec(self, num):
        self.queue.append(num)
        if num != self.value:
            self.unwanted += 1
       
        if self.left >= 0:
            if not self.unwanted:
                self.left += 1
                return True
            
            if self.queue[self.left] != self.value:
                self.unwanted -= 1

        self.left += 1

        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)