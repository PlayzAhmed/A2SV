# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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

    def find(self, word):
        cur = self.root
        ans = ""

        for ch in word:
            if ch not in cur.children:
                return word
            ans += ch
            cur = cur.children[ch]
            if cur.end:
                return ans

        q = deque([(cur, ans)])

        while q:
            cur, ans = q.popleft()
            if cur.end:
                break

            for ch, child in cur.children.items():
                q.append((child, ans+ch))
        
        return ans if len(ans) < len(word) else word


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        ans = []

        for word in dictionary:
            trie.add(word)

        for word in sentence.split():
            ans.append(trie.find(word))

        return " ".join(ans)