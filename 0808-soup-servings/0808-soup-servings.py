class Solution:
    def soupServings(self, n: int) -> float:
        self.dicts = {}
        n = ceil(n/25)
        for k in range(1,n+1):
            if self.calc(k,k) > 1 - 1e-5:
                return 1
        return self.calc(n,n)
    def calc(self,x,y):
        if (x,y) in self.dicts:
            return self.dicts[(x,y)]
        if not x and y:
            return 1
        if not x and not y:
            return 0.5
        if not x or not y:
            return 0
        curr = 0
        for idx in range(4):
            if idx == 0:
                curr += self.calc(max(0,x-4),y)
            elif idx == 1:
                curr += self.calc(max(0,x-3),max(0,y-1))
            elif idx == 2:
                curr += self.calc(max(0,x-2), max(0, y-2))
            else:
                curr += self.calc(max(0,x-1), max(0, y-3))
        self.dicts[(x,y)] = 0.25*curr
        return self.dicts[(x,y)]