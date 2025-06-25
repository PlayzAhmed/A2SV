# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution(object):
    def findMinDifference(self, timePoints):
        timePoints.sort()
        
        mn = 20000

        for i in range(len(timePoints)):
            firstH, firstM = map(int, timePoints[i].split(":"))
            secondH, secondM = map(int, timePoints[i-1].split(":"))
            timeDiff = abs((firstH * 60 + firstM) - (secondH * 60 + secondM))

            mn = min(mn, min(timeDiff, abs(timeDiff - 1440)))

        return mn