class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self, amount, coins):
        if amount== 0:
            return 0
        if amount not in self.dicts:
            minim = float("inf")
            for element in coins:
                val= amount - element
                if val >= 0:
                    minim = min(minim, self.solve(val,coins))
            self.dicts[amount] = minim + 1
        return self.dicts[amount] 
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        val = self.solve(amount, coins)
        if val == float("inf"):
            return -1
        return val
            
    