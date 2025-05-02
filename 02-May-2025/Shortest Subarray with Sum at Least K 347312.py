# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution(object):
    def shortestSubarray(self, nums, k):
        res = float('inf')
        maxEnding = 0
        q = deque()

        for r in range(len(nums)):
            maxEnding += nums[r]
            if maxEnding >= k:
                res = min(res, r + 1)

            while q and maxEnding - q[0][0] >= k:
                s, l = q.popleft()
                res = min(res, r - l)

            while q and q[-1][0] >= maxEnding:
                q.pop()

            q.append((maxEnding, r))


        return res if res != float('inf') else -1
        