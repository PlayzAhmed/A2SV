# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False
        self.val = 0

class MapSum(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, val):
        current = self.root

        for ch in key:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]

        current.end = True
        current.val = val
        

    def sum(self, prefix):
        ans = 0
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return ans
            current = current.children[ch]

        q = deque([current])

        while q:
            parent = q.popleft()

            ans += parent.val

            for child in parent.children.values():
                q.append(child)

        return ans

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)