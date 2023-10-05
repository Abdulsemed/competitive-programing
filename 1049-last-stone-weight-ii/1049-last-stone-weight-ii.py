class Solution:
    def __init__(self):
        self.minim = float("inf")
        self.dicts = {}
    def lastStoneWeightII(self, stones: List[int]) -> int:
        arr =[0]
        self.sums = sum(stones)
        
        self.dfs(0,0,stones)
        return self.minim
    def dfs(self,index, sums, stones):
        if index >= len(stones):
            val = self.sums - 2*(sums)
            if val > -1:
                self.minim = min(self.minim, val)
            return sums
        if (sums, index) in self.dicts:
            return self.dicts[(sums, index)]
        self.dicts[(sums,index)] = 1
        self.dfs(index+1, sums + stones[index], stones) 
        self.dfs(index+1, sums,stones)
    