class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        size1 = len(b)
        lps = [0]*(size1)
        prev = 0
        i = 1
        while i < size1:
            if b[prev] == b[i]:
                lps[i] = prev + 1
                i += 1
                prev += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev-1]
                    
        aIndex = bIndex = 0
        size2 = len(a)
        count = 1
        while bIndex < size1:
            if aIndex >= size2:
                aIndex = 0
                count += 1
            if a[aIndex] == b[bIndex]:
                aIndex += 1
                bIndex += 1
                
            elif count > 3:
                return -1
            else:
                if bIndex == 0:
                    aIndex += 1
                else:
                    bIndex = lps[bIndex-1]
                    
        return count