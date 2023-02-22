class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = {}
        for element in p:
            pDict[element] = 1 + pDict.get(element,0)
        sDict = {s[0]:1}
        left = 0
        right = 0
        size = len(s)
        sizep = len(p)
        result = []
        while right < size:
            if right-left+1 == sizep:
                if pDict == sDict:
                    result.append(left)
                sDict[s[left]] -= 1
                if sDict[s[left]] == 0:
                    del sDict[s[left]]
                left += 1
            right += 1
            if right < size:
                sDict[s[right]] = 1 + sDict.get(s[right], 0)
        return result