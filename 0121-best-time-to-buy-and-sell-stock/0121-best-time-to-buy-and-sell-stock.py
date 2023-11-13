class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0
        size = len(prices)
        prices[size-1] = (prices[size-1],prices[size-1])
        for index in range(size-2,-1,-1):
            if prices[index] < prices[index+1][1]:
                prices[index] = (prices[index],prices[index+1][1])
            else:
                prices[index] = (prices[index],prices[index])
        for index in range(size-1):
            maxim = max(prices[index+1][1] - prices[index][0], maxim)
            
        return maxim