class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxim = -1
        dicts = {}
        for index in range(len(s)):
            if s[index] in dicts:
                maxim = max((index-dicts[s[index]])-1, maxim)
            else:
                dicts[s[index]] = index
            
        return maxim
            