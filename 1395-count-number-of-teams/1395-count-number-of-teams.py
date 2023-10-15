class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)
        dp =[[1]*(2) for _ in range(size)]
        count = 0
        for index in range(size-2,-1,-1):
            for val in range(index+1,size):
                if rating[index] > rating[val]:
                    result = dp[val][0]
                    dp[index][0] += 1
                else:
                    result = dp[val][1]
                    dp[index][1] += 1
                if result >= 2:
                    count += (result -1)
   
            
        return count
                
                