# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.end = True
        

    def search(self, word):
        q = deque([self.root])

        for ch in word:
            lenQ = len(q)

            for _ in range(lenQ):
                cur = q.popleft()

                if ch == ".":
                    for child in cur.children.values():
                        q.append(child)
                else:
                    if ch not in cur.children:
                        continue
                    q.append(cur.children[ch])

            if not q:
                return False

        while q:
            cur = q.popleft()

            if cur.end:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)