class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum =[nums[0]]
        size= len(nums)
        for index in range(1,size):
            prefixSum.append(prefixSum[-1]+nums[index])
        return prefixSum