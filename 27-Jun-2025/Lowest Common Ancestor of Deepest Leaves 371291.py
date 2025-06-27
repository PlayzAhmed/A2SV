# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

class Solution(object):
    def lcaDeepestLeaves(self, root):
        self.nodes = []

        def dfs(node, depth=0, path=[root]):
            if not node.left and not node.right:
                if not self.nodes: self.nodes.append((depth, path+[node]))
                else:
                    if self.nodes[0][0] == depth: self.nodes.append((depth, path+[node]))
                    elif self.nodes[0][0] < depth: 
                        self.nodes = []
                        self.nodes.append((depth, path+[node]))
                return

            if node.left:
                dfs(node.left, depth+1, path+[node])
            if node.right:
                dfs(node.right, depth+1, path+[node])
        
        if not root.left and not root.right: return root

        if root.left: 
            dfs(root.left)

        if root.right:
            dfs(root.right)
        
        ans = None
        if self.nodes:
            _, left_path = self.nodes[0]
            _, right_path = self.nodes[-1]

            for left_node, right_node in zip(left_path, right_path):
                if left_node != right_node: break
                ans = left_node

        return ans