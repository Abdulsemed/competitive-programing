class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = []
        index = len(s)-1
        while s[index] == " ":
            index -= 1
            
        while index > -1 and s[index] != " ":
            ans.append(s[index])
            index -= 1
        return len(ans)