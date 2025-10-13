# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution(object):
    def findKthNumber(self, n, k):
        cur = 1
        k -= 1

        def helper(cur):
            ans = 0
            nei = cur + 1

            while cur <= n:
                ans += min(nei, n+1) - cur
                cur *= 10
                nei *= 10
        
            return ans

        while k > 0:
            steps = helper(cur)

            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur