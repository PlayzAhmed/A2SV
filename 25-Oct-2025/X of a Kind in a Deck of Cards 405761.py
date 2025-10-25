# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck = Counter(deck)
        ans = 0

        for x in deck.values():
            ans = gcd(ans, x)

        return ans > 1