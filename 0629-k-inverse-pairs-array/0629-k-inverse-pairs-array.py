class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        dicts = {}
        def f(n, k):
            if k==0: return 1
            if k<0 or n<=0: return 0
            if (n,k) in dicts:
                return dicts[(n,k)]
            dicts[(n,k)] = (f(n-1, k)+f(n, k-1)-f(n-1, k-n)+mod)%mod
            
            return dicts[(n,k)]
        return f(n, k)