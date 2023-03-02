class Solution:
    def bits(self,s,n):
        if n ==0:
            return [0]
        s = self.bits(s,n-1)
        
        temp = s.copy()
        for index in range(len(s)):
            if s[index] == 1:
                s[index] = 0
            else:
                s[index] = 1
        s = temp+[1] + s[::-1]
        return s
    def findKthBit(self, n: int, k: int) -> str:
        arr = self.bits([],n)
        return str(arr[k-1])