class Solution:
    def __init__(self):
        self.dicts = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in self.dicts:
            return self.dicts[n]
        self.dicts[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.dicts[n]
        
        