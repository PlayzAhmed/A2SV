# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        ans = []
        visited = set()
        heappush(heap, [nums1[0] + nums2[0], 0, 0])

        while len(ans) < k:
            sum_, i, j = heappop(heap)
            
            if (i, j) not in visited:
                visited.add((i, j))
                ans.append((nums1[i], nums2[j]))
                
                if i + 1 < len(nums1): heappush(heap, [nums1[i+1] + nums2[j], i+1, j])
                if j + 1 < len(nums2): heappush(heap, [nums1[i] + nums2[j+1], i, j+1])

        return ans
        