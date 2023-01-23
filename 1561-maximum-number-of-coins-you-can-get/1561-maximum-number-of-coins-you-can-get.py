class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        piles.sort()
        while len(piles)!=0:
            piles.pop()
            coins += piles.pop()
            piles.pop(0) 
        
        return coins