class Solution:
    def __init__(self):
        self.dicts = {} 
    def solve(self,index,flag,prices,fee):
        if index >= len(prices):
            return 0
        
        if (index,flag) in self.dicts:
            return self.dicts[(index,flag)]
        if flag:
            val1 = self.solve(index+1,False,prices,fee) + prices[index] - fee
            val2 = self.solve(index+1,True,prices,fee)
            
            maxim = max(val1,val2)
        else:
            val1 = self.solve(index+1,True,prices,fee) - prices[index]
            val2 = self.solve(index+1, False,prices,fee)
            maxim = max(val1,val2)
           
        self.dicts[(index,flag)] = maxim
        return self.dicts[(index, flag)]
                
    def maxProfit(self, prices: List[int], fee: int) -> int:
        maxim = max(0, self.solve(0,False,prices,fee))
        return maxim
        