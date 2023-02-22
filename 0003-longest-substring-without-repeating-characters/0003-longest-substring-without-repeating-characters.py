class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        sDict = {}
        size = len(s)
        maxLen = 0
        while right < size:
            sDict[s[right]] = 1 + sDict.get(s[right],0)
            while sDict[s[right]] > 1:
                sDict[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right -left +1)
            right += 1
        return maxLen