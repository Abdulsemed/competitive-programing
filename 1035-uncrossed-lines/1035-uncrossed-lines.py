class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-1]*(len(nums2)) for _ in range(len(nums1))]
        
        def dfs(i,j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 0
            for index in range(i, len(nums1)):
                for val in range(j, len(nums2)):
                    if nums1[index] == nums2[val]:
                        dp[i][j] = max(dp[i][j], dfs(index+1,val+1) + 1)
                        
            return dp[i][j]
        
        return dfs(0,0)
                        