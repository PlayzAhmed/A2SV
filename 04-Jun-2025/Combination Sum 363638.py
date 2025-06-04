# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        n = len(candidates)

        def backtrack(arr=[], s=0):
            if s == target:
                srt = sorted(arr)
                if srt not in ans:
                    ans.append(srt)
                return
            elif s > target:
                return

            for i in range(n):
                backtrack(arr + [candidates[i]], s + candidates[i])

        backtrack()
        return ans
                