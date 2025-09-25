# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.end = True

    def search(self, word, i=0):
        cur = self.root
        q = deque([(cur, i)])
        ans = []

        while q:
            cur, i = q.popleft()

            if cur.end:
                ans.append(i)

            if i >= len(word) or word[i] not in cur.children:
                continue

            q.append((cur.children[word[i]], i+1))

        return ans
    
class Solution(object):
    def wordBreak(self, s, wordDict):
        trie = Trie()
        q = deque([0])
        visited = set()

        for word in wordDict:
            trie.add(word)

        while q:
            i = q.popleft()
            if i in visited:
                continue
            visited.add(i)
            cur = trie.search(s, i)
            
            for x in cur:
                if x == len(s):
                    return True
                q.append(x)

        return False