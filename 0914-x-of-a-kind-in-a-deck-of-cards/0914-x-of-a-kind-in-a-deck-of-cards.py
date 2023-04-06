class Solution:
    def gcd(self, a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dicts= {}
        
        for num in deck:
            dicts[num] = 1 + dicts.get(num, 0)
        ans = float("inf")
        holder = -1
        if len(dicts) == 1 and list(dicts.values()) == [1]:
            return False
        for key in dicts:
            if holder == -1:
                holder = key
                continue
            if ans == float("inf"):
                val = self.gcd(dicts[key],dicts[holder])
            else:
                val = self.gcd(dicts[key], ans)
            if val == 1:
                return False
            ans = min(ans, val)
            
        return True