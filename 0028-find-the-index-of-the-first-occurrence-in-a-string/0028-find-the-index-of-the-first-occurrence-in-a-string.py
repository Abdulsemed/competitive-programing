class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle) -1
        if right >= len(haystack):
            return -1
        curr = 0
        search = 0
        
        for index in range(len(needle)-1,-1,-1):
            curr += (26 **(len(needle) -index -1)) *(ord(haystack[index])-96)
            search += (26 **(len(needle) -index -1)) *(ord(needle[index])-96)
            curr = curr % (1000000007)
            search = search % (1000000007) 
        while right <= len(haystack):
            if curr == search:
                return left
            else:
                if right + 1 >= len(haystack):
                    break
                curr = (curr - ((26**(len(needle)-1)) *(ord(haystack[left])-96))) * 26 + ord(haystack[right+1]) - 96
                curr = curr % (1000000007)
                left += 1
                right += 1
        return -1