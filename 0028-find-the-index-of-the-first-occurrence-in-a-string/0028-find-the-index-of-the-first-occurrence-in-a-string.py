class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size1 = len(needle)
        size2 = len(haystack)
        if size1 > size2:
            return -1
        lps = [0]*(size1)
        i = 1
        prev = 0
        while i < size1:
            if needle[prev] == needle[i]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev-1]
        index =0 
        i = 0
        while index < size2:
            if haystack[index] == needle[i]:
                index += 1
                i += 1
                if i == size1:
                    return index-(size1)
            else:
                if i == 0:
                    index += 1
                else:
                    i = lps[i-1]
            
        return -1