# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution(object):
    def continuousSubarrays(self, nums):
        mn, mx = float('inf'), float('-inf')
        freq = defaultdict(int)
        l = 0
        res = 0
        n = len(nums)

        for r in range(n):
            mn = min(nums[r], mn)
            mx = max(nums[r], mx)
            freq[nums[r]] += 1
            
            if abs(mn - mx) < 0 or abs(mn - mx) > 2:
                res += (r - l) * ((r - l)-1) // 2
                while abs(mn - mx) < 0 or abs(mn - mx) > 2:
                    freq[nums[l]] -= 1
                    if nums[l] == mn:
                        mn = min([x for x, y in freq.items() if y > 0])
                    elif nums[l] == mx:
                        mx = max([x for x, y in freq.items() if y > 0])

                    l += 1

                res -= (r - l) * ((r - l) - 1) // 2

        res += n + ((n - l) * ((n - l) - 1) // 2)
        
        return res
        