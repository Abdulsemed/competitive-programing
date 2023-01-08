class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        for index in range(size):
            ans.append(nums[nums[index]])
            
        return ans