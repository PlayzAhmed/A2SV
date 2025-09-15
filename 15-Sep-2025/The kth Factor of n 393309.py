# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution(object):
    def kthFactor(self, n, k):
        factors = [1]

        for i in range(2, n+1):
            if n % i == 0:
                factors.append(i)

        return factors[k-1] if len(factors) >= k else -1
        