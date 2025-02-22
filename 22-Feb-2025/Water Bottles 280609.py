# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange, drinks=0):
        if not drinks:
            return self.numWaterBottles(numBottles, numExchange, numBottles)
        elif numBottles >= numExchange:
            left = (numBottles%numExchange) + (numBottles//numExchange)
            return self.numWaterBottles(left, numExchange, drinks + (numBottles//numExchange))
        else:
            return drinks