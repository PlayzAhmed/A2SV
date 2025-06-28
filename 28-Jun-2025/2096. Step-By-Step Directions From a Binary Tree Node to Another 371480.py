# Problem: 2096. Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=problem-list-v2&envId=depth-first-search

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        
        def dfs(node, target, path=deque()):
            if not node: return False
            if node.val == target: return path
            
            path.append("L")
            ans = dfs(node.left, target, path)
            if ans:
                return ans
            path.pop()

            path.append("R")
            ans = dfs(node.right, target, path)
            if ans:
                return ans
            path.pop()

        first = dfs(root, startValue)
        sec = dfs(root, destValue, deque())
        res = ""

        while first and sec and first[0] == sec[0]:
            first.popleft()
            sec.popleft()

        while first:
            first.pop()
            res += "U"

        while sec:
            res += sec.popleft()

        return res