class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]+1
        index = 0
        dp = [0]*(maxDay)
        for day in range(1,maxDay):
            if day < days[index]:
                dp[day] = dp[day-1]
            else:
                index += 1
                
                dp[day] = min(
                    dp[day-1] + costs[0],
                    dp[max(0,day-7)] + costs[1],
                    dp[max(0,day-30)] + costs[2]
                )
        return dp[-1]