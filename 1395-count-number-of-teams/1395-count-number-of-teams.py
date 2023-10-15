class Solution:
    def __init__(self):
        self.dicts = defaultdict(int)
        self.ans = 0
    def numTeams(self, rating: List[int]) -> int:
        self.dfs(0,rating,rating[0] > rating[1])
        return self.ans
    def dfs(self,index,rating,flag):
        
        if (index,flag) in self.dicts:
            return self.dicts[(index,flag)]
        
        for val in range(index+1, len(rating)):
            if rating[index] > rating[val]:
                result = self.dfs(val,rating,True)
                self.dicts[(index,True)] += 1
            else:
                result = self.dfs(val,rating,False)
                self.dicts[(index,False)] += 1
                
            if result >= 2:
                self.ans += (result-2 + 1)
        self.dicts[(index,True)] += 1
        self.dicts[(index,False)] += 1
        return self.dicts[(index, flag)]