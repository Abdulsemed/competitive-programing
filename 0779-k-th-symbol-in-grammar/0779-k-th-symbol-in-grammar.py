class Solution:
    def inverse(self,n):
        if n == 1:
            return 0
        return 1
    def middleware(self,n,k):
        if n == 1:
            return 0
        size = 2**(n-1)
        mid = size//2
        if k > mid:
            return self.inverse(self.middleware(n-1,k-mid))
        return self.middleware(n-1,k)
        
    def kthGrammar(self, n: int, k: int) -> int:
        return self.middleware(n,k)
        