# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        self.timeToLive = timeToLive
        self.tokens = defaultdict(int)
        

    def generate(self, tokenId, currentTime):
        self.tokens[tokenId] = currentTime+self.timeToLive
        

    def renew(self, tokenId, currentTime):
        if self.tokens[tokenId] > currentTime:
            self.generate(tokenId, currentTime)

        

    def countUnexpiredTokens(self, currentTime):
        res = 0
        for time in self.tokens.values():
            if time > currentTime:
                res += 1

        return res