class Solution:
    def __init__(self):
        self.condition = True
    def check(self, n, bools):
        if bools:
            if n & 1 == 0:
                n >>= 1
            else:
                self.condition = False
        else:
            if n & 1 != 0:
                n >>= 1
            else:
                self.condition = False
        return n, self.condition
    def hasAlternatingBits(self, n: int) -> bool:
        bools = False
        if n & 1 == 0:
            bools = True
        while n and self.condition:
            n, self.condition = self.check(n,bools)
            bools = not bools
        return self.condition
        