# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        parents = defaultdict(TreeNode)
        q = deque()
        visited = set()
        ans = []
        
        def get_parent(node, parent):
            if not node: return

            parents[node] = parent

            get_parent(node.left, node)
            get_parent(node.right, node)
        
        get_parent(root, None)
        parents[root] = None

        q.append([target, 0])

        while q:
            node, d = q.popleft()
            if node is None or node in visited: continue
            if d > k: break
            if node.val == 0: print(node)
            if d == k: 
                ans.append(node.val)
                continue

            visited.add(node)

            q.append([node.left, d+1])
            q.append([node.right, d+1])
            q.append([parents[node], d+1])

        return ans

