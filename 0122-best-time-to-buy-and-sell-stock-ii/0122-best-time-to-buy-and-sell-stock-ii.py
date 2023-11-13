class Solution:
    def __init__(self):
        self.dicts = {}
        
    def maxProfit(self, prices: List[int]) -> int:
        self.dfs(0,False,prices)
        return max(0, self.dicts[(0,False)])
    def dfs(self,index,flag,prices):
        
        if index >= len(prices):
            return 0
        if(index, flag) in self.dicts:
            return self.dicts[(index,flag)]
        
        if flag:
            val1 = self.dfs(index+1,False,prices) + prices[index]
            val2 = self.dfs(index+1,True,prices)
        else:
            val1 = self.dfs(index+1,True,prices) - prices[index]
            val2 = self.dfs(index+1,False,prices)
        self.dicts[(index,flag)] = max(val1,val2)
        
        return self.dicts[(index,flag)]
            
            
        