# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem(object):

    def __init__(self):
        self.checkin = defaultdict(list)
        self.avg = defaultdict(list)

    def checkIn(self, id, stationName, t):
        self.checkin[id] = [stationName, t]


        

    def checkOut(self, id, stationName, t):
        all_time, all_count = 0.0, 0.0
        if self.avg[" ".join([self.checkin[id][0], stationName])]:
            all_time = self.avg[" ".join([self.checkin[id][0], stationName])][0]
            all_count = self.avg[" ".join([self.checkin[id][0], stationName])][1]
        
        all_time += t - self.checkin[id][1]
        all_count += 1
        self.avg[" ".join([self.checkin[id][0], stationName])] = [all_time, all_count]
        

    def getAverageTime(self, startStation, endStation):
        return self.avg[" ".join([startStation, endStation])][0] / self.avg[" ".join([startStation, endStation])][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)