# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution(object):
    def maxKelements(self, nums, k):
        heap = []
        ans = 0

        for x in nums:
            heappush(heap, -x)

        while k:
            x = -heappop(heap)
            ans += x
            heappush(heap, -ceil(float(x)/3.0))
            k -= 1 

        return int(ans)
        