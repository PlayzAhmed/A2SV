# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        path = path.replace("/", " ").split()
        stack = []

        for x in path:
            if x == ".." and stack:
                stack.pop()
            elif x != ".." and x != ".":
                stack.append(x)

        return "/" + "/".join(stack)
        