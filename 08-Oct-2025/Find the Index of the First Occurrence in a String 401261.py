# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(needle), len(haystack)
        if not n: return n
        if m < n: return -1

        BASE = 27
        MOD = 10 ** 9 + 7
        power = pow(BASE, n-1)

        def compute_hash(s):
            h = 0

            for ch in s:
                h = (h*BASE + (ord(ch)-26)) % MOD

            return h

        target_hash = compute_hash(needle)
        cur_hash = compute_hash(haystack[:n])

        if target_hash == cur_hash and needle == haystack[:n]:
            return 0

        for i in range(n, m):
            old_char = (ord(haystack[i-n]) - 26) * power % MOD
            cur_hash = (cur_hash - old_char + MOD) % MOD
            cur_hash = (cur_hash * BASE + (ord(haystack[i]) - 26)) % MOD

            start = i - n + 1 

            if cur_hash == target_hash and needle == haystack[start:i+1]:
                return start

        return -1