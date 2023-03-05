class Solution:
    def minimumWindow(self,s,tDict):
        left = 0
        right = 0
        valleft = 0
        valright = 0
        minLen = len(s)
        size = len(s)
        sDict = {}
        s2Dict = {}
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
        return minLen
    def balancedString(self, s: str) -> int:
        size = len(s)//4
        dict1 = {"Q":-size, "W":-size, "E":-size, "R":-size}
        for element in s:
            dict1[element] = 1 + dict1.get(element,0)
        if dict1["Q"] < 1: del dict1["Q"]
        if dict1["E"] < 1: del dict1["E"]
        if dict1["W"] < 1: del dict1["W"]
        if dict1["R"] < 1: del dict1["R"]
        if dict1:
            return self.minimumWindow(s,dict1)
        return 0