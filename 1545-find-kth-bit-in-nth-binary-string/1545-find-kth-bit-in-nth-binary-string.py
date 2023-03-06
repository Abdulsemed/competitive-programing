class Solution:
    def inverse(self,s):
        if s == "1":
            return "0"
        return "1"
    def bits(self,n,k):
        if n == 1:
            return "0"
        size = (2**n)-1
        mid = math.ceil(size/2)
        if k == mid:
            return "1"
        elif k < mid:
            return self.bits(n-1,k)
        else:
            return self.inverse(self.bits(n-1,size-k+1))
    def findKthBit(self, n: int, k: int) -> str:
        return self.bits(n,k)