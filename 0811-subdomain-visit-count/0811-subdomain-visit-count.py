class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict = {}
        resultDomains = []
        for element in cpdomains:
            counts, domain = element.split(" ")
            domains = domain.split(".")
            domainDict[domain] = int(counts) + domainDict.get(domain, 0)
            domainDict[domains[-1]]= int(counts) + domainDict.get(domains[-1], 0)
            if len(domains) > 2:
                lists = [domains[1],domains[2]]
                newDomain = '.'.join(lists)
                domainDict[newDomain]= int(counts) + domainDict.get(newDomain, 0)
            
        for domain in domainDict:
            lists = [str(domainDict[domain])]
            lists.append(domain)
            domainDict[domain] = ' '.join(lists)
            
        return domainDict.values()