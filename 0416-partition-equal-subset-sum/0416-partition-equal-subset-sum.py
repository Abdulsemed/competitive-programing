class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,index, sums,nums):
        if index >= len(nums) or sums <= 0 :
            return sums == 0
        if (sums, index) in self.dicts:
            return False
        self.dicts[(sums,index)] = 1
        return self.solve(index+1, sums - nums[index], nums) or self.solve(index+1, sums,nums)
            
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        return sums%2 == 0 and self.solve(0, sums//2, nums)