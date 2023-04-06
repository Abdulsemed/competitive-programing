class Solution:
    def gcd(self, a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dicts= {}
        
        for num in deck:
            dicts[num] = 1 + dicts.get(num, 0)
        if reduce(self.gcd, dicts.values()) > 1:
            return True
        return False
        