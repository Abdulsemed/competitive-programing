class Solution:
    def countOrders(self, n: int) -> int:
        start = 1
        for index in range(2,n+1):
            val = index * 2
            curr =  (val *(val-1))//2
            start = start * curr
            
        return start % (10**9 + 7)