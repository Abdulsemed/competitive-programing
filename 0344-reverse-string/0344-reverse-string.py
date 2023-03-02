class Solution:
    def reverso(self,s, l, r):
        if l == r or l > r:
            return s
        s= self.reverso(s,l+1, r-1)
        s[l], s[r] = s[r], s[l]
        return s
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = self.reverso(s,0,len(s)-1)
        return s
        