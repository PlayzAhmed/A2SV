# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 0

        cap = capacity

        for i in range(len(plants)):
            if plants[i] > cap:
                steps += i + i + 1
                cap = capacity - plants[i]
            else:
                cap -= plants[i]
                steps += 1

        return steps
        