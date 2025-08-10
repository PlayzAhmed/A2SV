# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        dp = {}

        def dfs(i=0):
            if i in dp: return dp[i]
            if i == len(s): return 1
            if s[i] == "0": return 0

            ans = dfs(i+1)

            if i + 1 < len(s) and int(s[i:i+2]) < 27:
                ans += dfs(i+2)

            dp[i] = ans
            return ans

        return dfs()
