# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                string = ""
                num = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string

                stack.pop()

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(string * int(num))
                
            else:
                stack.append(s[i])

        return "".join(stack)