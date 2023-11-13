def __init__(self):
self.dicts = {}
self.maxim = 0
def maxProfit(self, prices: List[int]) -> int:
self.dfs(0,False,prices,0)
return self.maxim
def dfs(self,index,flag,prices,idx):
if index >= len(prices):
return 0
if(idx, flag) in self.dicts:
return self.dicts[(idx,flag)]
if flag:
val1 = prices[index] - prices[idx]
val2 = self.dfs(index+1,True,prices,idx)
self.maxim = max(self.maxim,val1)
else:
val1 = self.dfs(index+1,True,prices,idx)
val2 = self.dfs(index+1,False,prices,index+1)
self.dicts[(idx,flag)] = max(val1,val2)
return self.dicts[(idx,flag)]