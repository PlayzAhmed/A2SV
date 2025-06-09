# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        mp = {
            "": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) < 2:
            return mp[digits]
        
        ans = []

        def dfs(i=0, cur=""):
            if i >= len(digits):
                ans.append(cur)
                return

            for ch in mp[digits[i]]:
                dfs(i+1, cur+ch)

        dfs()
        return ans
        