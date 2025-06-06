# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        ans = []
        def backtrack(idx):
            if idx == -1:
                return

            if ans:
                for _ in range(len(ans)):
                    num = ans.pop(0)

                    for i in range(len(num)+1):
                        num.insert(i, nums[idx])
                        ans.append(num+[])
                        num.pop(i)
            else:
                ans.append([nums[idx]])

            return backtrack(idx-1)
        
        backtrack(len(nums)-1)
        return ans
