# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []

        for x in stones:
            heappush(heap, -x)

        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)

            if x > y:
                heappush(heap, y-x)
            elif x < y:
                heappush(heap, x-y)        

        return -heap[0] if heap else 0