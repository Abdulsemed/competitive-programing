class Solution:
    def solve(self,n,dicts):
        if n== 1:
            return 1
        if n == 0:
            return 0
        if n in dicts:
            return dicts[n]
        dicts[n] = self.fib(n-1) + self.fib(n-2)
        return dicts[n]
    
    def fib(self, n: int) -> int:
        dicts = {}
        return self.solve(n,dicts)