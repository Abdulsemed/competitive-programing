class Solution:
    def __init__(self):
        self.count = 0
        self.dicts = {}
    def climbing(self, n, cost):
        if n== 0 or n == 1:
            return cost[n]
        if n in self.dicts:
            return self.dicts[n]
        self.dicts[n] = min(self.climbing(n-1,cost), self.climbing(n-2, cost))
        if n < len(cost):
            self.dicts[n] += cost[n]
        return self.dicts[n]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.climbing(len(cost),cost)
        return self.dicts[len(cost)]