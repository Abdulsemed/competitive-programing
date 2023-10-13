class Solution:
    def longestPrefix(self, s: str) -> str:
        size = len(s)
        lps = [0] *(size)
        prev = 0
        i = 1
        while i < size:
            if s[i] == s[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev-1]          
        return s[:lps[-1]]