# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        freq = Counter(s)
        counter = set()
        stack = []

        for i in range(len(s)):
            if s[i] in counter:
                freq[s[i]] -= 1
                continue

            while stack and stack[-1] >= s[i] and freq[stack[-1]] - 1 > 0 and s[i] not in counter:
                x = stack.pop()
                freq[x] -= 1
                counter.remove(x)
                

            if s[i] not in counter:
                counter.add(s[i])
                stack.append(s[i])
            

        return "".join(stack)