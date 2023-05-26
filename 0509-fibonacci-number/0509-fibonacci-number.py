class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,n,dicts):
        if n== 1:
            return 1
        if n == 0:
            return 0
        if n not in dicts:
            dicts[n] = self.solve(n-1, dicts) + self.solve(n-2, dicts)
        return dicts[n]
    
    def fib(self, n: int) -> int:
        dicts = {}
        return self.solve(n,dicts)