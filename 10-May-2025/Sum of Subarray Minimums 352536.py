# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = pow(10, 9) + 7
        stack = []
        res = 0

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                res = (res + arr[j] * left * right) % MOD

            stack.append(i)


        for i in range(len(stack)):
            left = stack[i] - stack[i-1] if i > 0 else stack[i] + 1
            right = len(arr) - stack[i]
            res = (res + arr[stack[i]] * left * right) % MOD

        return res
        