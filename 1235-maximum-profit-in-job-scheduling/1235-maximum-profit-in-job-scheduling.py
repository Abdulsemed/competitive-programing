class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        for index in range(len(endTime)):
            endTime[index] = [startTime[index],endTime[index],profit[index]]
        endTime.sort(key = lambda x:(x[0],x[1]))
        dp = [0] * (len(startTime)+1)
        for index in range(len(startTime)-1,-1,-1):
            left = index
            right = len(startTime)-1
            value = endTime[index][1]
            while left<= right:
                mid = left + (right-left)//2
                if endTime[mid][0] >= value:
                    right = mid -1
                else:
                    left = mid + 1
            dp[index] =  max(endTime[index][2] + dp[left], dp[index+1])
            
        return dp[0]