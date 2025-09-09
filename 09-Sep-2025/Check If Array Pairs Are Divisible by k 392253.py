# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution(object):
    def canArrange(self, arr, k):
        freq = defaultdict(int)

        for x in arr:
            freq[x % k] += 1

        if freq[0] % 2 != 0: return False
        
        for x in range(1, k):
            if freq[x] != freq[k-x]: return False

        return True
        