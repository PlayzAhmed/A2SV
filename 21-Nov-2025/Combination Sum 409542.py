# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        n = len(candidates)

        def backtrack(i=0, arr=[], total=0):
            if total == target:
                ans.append(arr + [])
                return
            elif i >= n or total > target:
                return

            arr.append(candidates[i])
            backtrack(i, arr, total + candidates[i])
            arr.pop()
            backtrack(i+1, arr, total)

        backtrack()
        return ans
                