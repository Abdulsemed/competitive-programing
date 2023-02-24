class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sDict = {}
        left = 0
        size = len(s)
        maxLen = 0
        for right in range(size):
            sDict[s[right]] = 1 + sDict.get(s[right], 0)
            if len(sDict) < 1:
                continue
            if sum(sDict.values()) -max(sDict.values())> k:
                sDict[s[left]] -= 1
                if sDict[s[left]] == 0:
                    del sDict[s[left]]
                left += 1
            maxLen = max(maxLen, sum(sDict.values()))
        return maxLen