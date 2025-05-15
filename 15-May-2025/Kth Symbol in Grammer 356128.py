# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution(object):
    def kthGrammar(self, n, k):
        left, right = 1, pow(2, n-1)
        cur = 0
        while left < right:
            mid = (left + right) // 2

            if mid >= k:
                right = mid
            else:
                left = mid + 1
                cur = not cur
        
        return int(cur)