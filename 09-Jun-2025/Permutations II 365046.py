# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution(object):
    def permuteUnique(self, nums):
        ans = []
        perm = []
        freq = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                ans.append(perm+[])
                return

            for n in freq:
                if freq[n] > 0:
                    perm.append(n)
                    freq[n] -= 1
                    dfs()
                    freq[n] += 1
                    perm.pop()
        
        dfs()
        return ans