class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index in range(len(s)):
            if count[s[index]] == 1:
                return index
        return -1