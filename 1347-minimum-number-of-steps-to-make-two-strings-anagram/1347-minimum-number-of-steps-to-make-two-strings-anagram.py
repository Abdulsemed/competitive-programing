class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dicts1 = {}
        dicts2 = {}
        for index in range(len(s)):
            dicts1[s[index]] = 1 + dicts1.get(s[index], 0)
            dicts2[t[index]] = 1 + dicts2.get(t[index], 0)
            
        count = 0
        for key in dicts1:
            curr = 0
            if key in dicts2:
                curr = dicts2[key]
            count += max((dicts1[key] - curr), 0)
        
        return count