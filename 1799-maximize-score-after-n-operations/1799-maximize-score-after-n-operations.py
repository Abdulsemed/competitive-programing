class Solution:
    def __init__(self):
        self.size = 0
        self.gcds = {}
        self.maxim = - float("inf")
    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def maxScore(self, nums: List[int]) -> int:
        self.visited = 0
        dp = defaultdict(int)
        
        def dfs(mul):
            if self.visited in dp:
                return dp[self.visited]
            curr = self.visited
            for index in range(len(nums)):
                for val in range(index+1,len(nums)):
                    if index != val:
                        if self.visited & (1 << index) == 0 and self.visited & (1 << val)== 0:
                            
                            self.visited = self.visited ^ (1 << index)
                            self.visited = self.visited ^ (1 << val)
                            if (nums[index], nums[val]) not in self.gcds:
                                self.gcds[(nums[index], nums[val])] = self.gcd(nums[index], nums[val])
                            score = mul * self.gcds[(nums[index], nums[val])]
            
                            dp[curr] = max(dp[curr], score + dfs(mul+1))
                            
                            self.visited = self.visited ^ (1 << index )
                            self.visited = self.visited ^ (1 << val)
            
            return dp[curr]
        return dfs(1)