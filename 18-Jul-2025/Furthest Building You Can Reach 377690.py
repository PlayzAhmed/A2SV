# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                bricks -= diff
                heappush(heap, -diff)

                if bricks < 0:
                    bricks += -heappop(heap)
                    ladders -= 1

                if ladders < 0:
                    return i

        return len(heights)-1
            