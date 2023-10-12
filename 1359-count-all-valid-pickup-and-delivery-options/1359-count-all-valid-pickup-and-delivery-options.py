class Solution:
    def multiply(self, a, b, m):
        return ((a % m) * (b % m)) % m
    def countOrders(self, n: int) -> int:
        start = 1
        mod = 10**9 + 7
        for index in range(2,n+1):
            val = index * 2
            curr =  self.multiply(val,val-1,mod)//2
            start = self.multiply(start, curr,mod)
            
        return start % (mod)