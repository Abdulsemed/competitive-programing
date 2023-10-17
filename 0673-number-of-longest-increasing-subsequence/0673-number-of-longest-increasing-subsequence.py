class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [[1 for _ in range(2)] for _ in range(size)]
        count = 0
        for index in range(size-2,-1,-1):
            for val in range(index+1,size):
                curr = 1
                now = 1
                if nums[index] < nums[val]:
                    curr += dp[val][0]
                    now = dp[val][1]
                    if dp[index][0] < curr:
                        dp[index][0] = curr
                        dp[index][1] = now
                    elif dp[index][0] == curr:
                        dp[index][1] += now 
 
        dp.sort(reverse = True)
        num = dp[0][0]
        count = dp[0][1]
        for index in range(1,size):
            if num == dp[index][0]:
                count += dp[index][1]
            else:
                break
                
        return count