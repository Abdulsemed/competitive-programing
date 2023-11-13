class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0
        size = len(prices)
        newPrices = [prices[-1]]
        for index in range(size-2,-1,-1):
            if prices[index] < newPrices[-1]:
                newPrices.append(newPrices[-1])
            else:
                newPrices.append(prices[index])
        for index in range(size-1):
            maxim = max(newPrices[size-index-1] - prices[index], maxim)
            
        return maxim