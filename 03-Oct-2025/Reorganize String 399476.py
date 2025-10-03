# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution(object):
    def reorganizeString(self, s):
        heap = [(-x, w) for w, x in Counter(s).items()]
        heapify(heap)

        ans = ""

        while heap:
            x, w = heappop(heap)

            if ans and ans[-1] == w:
                return ""
            ans += w

            if heap:
                y, z = heappop(heap)
                ans += z
                if y + 1:
                    heappush(heap, (y+1, z))

            if x + 1:
                heappush(heap, (x+1, w))
        
        return ans