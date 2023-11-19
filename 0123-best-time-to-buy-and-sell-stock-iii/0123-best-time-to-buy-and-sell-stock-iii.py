class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -float("inf")
        sell = 0
        buy2 = -float("inf")
        answer = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell = max(sell, price+buy1)
            buy2 = max(buy2, sell-price)
            answer = max(answer, price + buy2)
            
        return answer