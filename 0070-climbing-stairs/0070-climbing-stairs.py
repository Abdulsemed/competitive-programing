class Solution:
    def solve(self,n,dicts):
        if n== 1:
            return 1
        if n == 2:
            return 2
        if n not in dicts:
            dicts[n] = self.solve(n-1, dicts) + self.solve(n-2, dicts)
        return dicts[n]
    def climbStairs(self, n: int) -> int:
        dicts ={}
        return self.solve(n,dicts)