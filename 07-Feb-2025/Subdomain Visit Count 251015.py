# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        res = {}

        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            visits = int(cpdomain[0])
            domains = cpdomain[1].split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                if domain in res:
                    res[domain] += visits
                else:
                    res[domain] = visits

        return [str(y) + ' ' + x for x, y in res.items()]

        