class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts = {}
        visited = set()
        for index in range(len(s)):
            if s[index] not in dicts and s[index] != t[index]:
                if t[index] not in visited :
                    dicts[s[index]] = t[index]
                    visited.add(t[index])
                else:
                    return False
            elif s[index] in dicts:
                if dicts[s[index]] != t[index]:
                    return False
            else:
                if t[index] in visited: return False
                dicts[s[index]] = s[index]
                visited.add(s[index])
                    
        return True