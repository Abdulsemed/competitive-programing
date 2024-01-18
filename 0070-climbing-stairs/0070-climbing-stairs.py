class Solution:
    def climbStairs(self, n: int) -> int:
        val1 = 1
        val2 = 0
        for index in range(n):
            curr = val1
            val1 = val2 + val1
            val2 = curr
            
        return val1