class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        for index in range(len(scores)):
            scores[index] = [ages[index], scores[index]]
        scores.sort(key = lambda x:(x[0],x[1]), reverse = True)
        dp = deepcopy(scores)
        ans = scores[len(scores)-1][1]
        for index in range(len(scores)-2,-1,-1):
            for val in range(index+1,len(scores)):
                curr = 0
                
                if scores[index][1] >= scores[val][1] or scores[index][0] == scores[val][0]:
                    curr += dp[val][1]
                if scores[index][1] + curr > dp[index][1]:
                    dp[index][1] = scores[index][1] + curr
                    
            ans = max(ans, dp[index][1]) 
        return ans