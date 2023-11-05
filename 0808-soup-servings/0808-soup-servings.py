class Solution:
    def soupServings(self, n: int) -> float:
        self.dicts = {}
        if n < 10000:
            return self.calc(n,n)
        return 1
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
                curr += self.calc(max(0,x-100),y)
            elif idx == 1:
                curr += self.calc(max(0,x-75),max(0,y-25))
            elif idx == 2:
                curr += self.calc(max(0,x-50), max(0, y-50))
            else:
                curr += self.calc(max(0,x-25), max(0, y-75))
        self.dicts[(x,y)] = 0.25*curr
        return self.dicts[(x,y)]