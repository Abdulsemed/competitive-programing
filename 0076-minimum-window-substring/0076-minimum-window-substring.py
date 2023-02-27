class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        valleft = 0
        valright = 0
        minLen = len(s)
        size = len(s)
        sDict = {}
        tDict = {}
        s2Dict = {}
        for element in t:
            tDict[element] = 1 + tDict.get(element,0)
        while right < size:
            if s2Dict != tDict:
                if s[right] in tDict:
                    sDict[s[right]] = 1 + sDict.get(s[right], 0)
                    s2Dict[s[right]] = 1 + s2Dict.get(s[right], 0)
                    if tDict[s[right]] < s2Dict[s[right]]:
                        s2Dict[s[right]] -= 1
                right += 1
            while s2Dict == tDict:
                if minLen >= right -left:
                    valleft = left
                    valright = right
                    minLen = right -left
                if s[left] in tDict:
                    sDict[s[left]] -= 1
                    if sDict[s[left]] < tDict[s[left]]:
                        s2Dict[s[left]] -= 1
                left += 1
        return s[valleft:valright]
            