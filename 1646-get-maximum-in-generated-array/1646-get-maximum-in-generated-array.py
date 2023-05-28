class Solution:
    def __init__(self):
        self.dicts = {}
        self.maxim = -float("inf")
    def getMaximum(self, n: int) -> int:
        if n == 0:
            self.maxim = max(self.maxim, 0)
            return 0
        if n == 1:
            self.maxim = max(self.maxim, 1)
            return 1
        if n in self.dicts:
            self.maxim = max(self.maxim, self.dicts[n])
            return self.dicts[n]
        if  n % 2:
            self.dicts[n] = self.getMaximum(n//2) + self.getMaximum(n-n//2)
        else:
            self.dicts[n] = self.getMaximum(n//2)
        self.maxim = max(self.maxim, self.dicts[n])
        return self.dicts[n]
    def getMaximumGenerated(self, n: int) -> int:
        for index in range(n,-1,-1):
            self.getMaximum(index)
        return self.maxim
        
            
        