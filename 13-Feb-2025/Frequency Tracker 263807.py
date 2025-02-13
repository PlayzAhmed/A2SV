# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker(object):

    def __init__(self):
        self.mp = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number):
        # print("mp: ", self.mp)
        # print("freq: ", self.freq)
        if self.mp[number]:
            self.freq[self.mp[number]] -= 1

        self.mp[number] += 1
        self.freq[self.mp[number]] += 1

    def deleteOne(self, number):
        # print("mp: ", self.mp)
        # print("freq: ", self.freq)
        if self.mp[number]:
            self.mp[number] -= 1
            self.freq[self.mp[number]] += 1
            if self.freq[self.mp[number]+1]:
                self.freq[self.mp[number]+1] -= 1
        

    def hasFrequency(self, frequency):
        # print("mp: ", self.mp)
        # print("freq: ", self.freq)
        if self.freq[frequency] > 0:
            return True

        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)