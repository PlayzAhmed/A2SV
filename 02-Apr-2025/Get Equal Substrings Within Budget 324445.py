# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        n = len(s)
        pre = [abs(ord(s[0])-ord(t[0]))]

        for i in range(1, n):
            pre.append(abs(ord(s[i])-ord(t[i])) + pre[-1])

        mx = 0
        l = -1

        for r in range(n):
            if l == -1:
                if pre[r] > maxCost:
                    l += 1
                    while pre[r] - pre[l] > maxCost and l < r-1:
                        l += 1
                    if pre[r] - pre[l] <= maxCost:
                        mx = max(mx, r - l)
                else:
                    mx = max(mx, r + 1)
            else:
                while pre[r] - pre[l] > maxCost and l < r-1:
                    l += 1

                if pre[r] - pre[l] <= maxCost:
                    mx = max(mx, r - l)

        return mx