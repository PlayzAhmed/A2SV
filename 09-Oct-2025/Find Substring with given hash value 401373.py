# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution(object):
    def subStrHash(self, s, BASE, MOD, k, target):
        n = len(s)
        cur = 0
        ans = ""
        
        for i in range(n-1, n-k-1, -1):
            cur = (cur * BASE + (ord(s[i])-96)) % MOD
        
        if cur == target:
            ans = s[n-k:]

        POW = pow(BASE, k-1)

        for i in range(n-k-1, -1, -1):
            old = (ord(s[i+k]) - 96) * POW
            cur = (cur - old + MOD) % MOD
            cur = (cur * BASE + (ord(s[i])-96)) % MOD

            if cur == target:
                ans = s[i:i+k]

        return ans