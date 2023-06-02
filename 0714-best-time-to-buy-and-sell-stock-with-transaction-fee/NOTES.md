class Solution:
def __init__(self):
self.dicts = {}
def solve(self,index,prices,fee):
if index >= len(prices):
return 0
if index in self.dicts:
return self.dicts[index]
maxim = 0
for val in range(index+1,len(prices)):
ans = self.solve(val,prices,fee)
maxim = max(maxim, ans+(prices[val]-prices[index]-fee), ans)
self.dicts[index] = maxim
return self.dicts[index]
def maxProfit(self, prices: List[int], fee: int) -> int:
maxim = max(0, self.solve(0,prices,fee))
return maxim