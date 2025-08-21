# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        ans =[[]]
        q = deque()

        for i in range(len(nums)):
            q.append(([nums[i]], i+1))
            ans.append([nums[i]])

        while q:
            num, i = q.popleft()

            if i >= len(nums):
                if num not in ans:
                    ans.append(num)

                continue

            q.append((num, i+1))
            q.append((num+[nums[i]], i+1))

        return ans