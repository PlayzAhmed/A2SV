# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert_and_display(self, word):
        cur = self.root
        path = ""
        ans = []

        for ch in word:
            path += ch

            if ch not in cur.children:
                cur.children[ch] = TrieNode()
                cur = cur.children[ch]
                cur.end = True
                cur = self.root
                ans.append(path)
                path = ""
                continue

            cur = cur.children[ch]

        return ans

class Solution(object):
    def partitionString(self, s):
        trie = Trie()
        return trie.insert_and_display(s)
        