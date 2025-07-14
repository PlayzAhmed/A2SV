# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        nums = Counter(nums)
        heap = []
        res = []

        for val, freq in nums.items():
            heappush(heap, (-freq, val))

        while k:
            _, val = heappop(heap)
            res.append(val)
            k -= 1

        return res
        