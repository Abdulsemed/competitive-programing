class Solution:
    def partitionString(self, s: str) -> int:
        dicts = {}
        left = 0
        right = 0
        count = 0
        while right < len(s):
            if s[right] in dicts:
                dicts = {}
                left = right
                count += 1
            dicts[s[right]] = 1
            right += 1
    
        return count+1