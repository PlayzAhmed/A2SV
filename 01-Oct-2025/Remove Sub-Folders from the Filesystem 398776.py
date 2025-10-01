# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, f):
        cur = self.root

        if not f: return

        for x in f:
            if cur.end: return
            if x not in cur.children:
                cur.children[x] = TrieNode()
            cur = cur.children[x]

        cur.end = True

    def display(self):
        ans = []
        q = deque([(self.root, "")])

        while q:
            cur, path = q.popleft()
            if cur.end:
                ans.append(path)
                continue

            for node, child in cur.children.items():
                q.append((child, path + "/" + node))

        return ans

class Solution(object):
    def removeSubfolders(self, folder):
        trie = Trie()

        for path in folder:
            path = path.split("/")
            trie.insert(path[1:])
        
        return trie.display()