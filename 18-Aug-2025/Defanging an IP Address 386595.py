# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution(object):
    def defangIPaddr(self, address):
        return "[.]".join(address.split("."))
        