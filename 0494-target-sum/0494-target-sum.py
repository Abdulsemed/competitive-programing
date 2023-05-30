class Solution:
    def __init__(self):
        self.count = 0
        self.dicts = defaultdict(int)
    def solve(self,index, sums,target,nums):
        if index>= len(nums):
            if sums == target:
                return 1
            return 0
        if (index, sums) not in self.dicts:
            self.dicts[(index,sums)] += self.solve(index+1,sums+nums[index],target,nums)
            self.dicts[(index,sums)] += self.solve(index+1,sums-nums[index],target,nums)
        return self.dicts[(index,sums)]
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solve(0,0,target,nums)