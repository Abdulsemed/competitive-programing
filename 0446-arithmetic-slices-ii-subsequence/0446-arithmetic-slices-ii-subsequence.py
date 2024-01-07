class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        count = 0
        for index in range(len(nums)-1,-1,-1):
            for val in range(index+1,len(nums)):
                diff = nums[index] - nums[val]
                dp[(index,diff)] += dp[(val,diff)]+1
                count += dp[(val,diff)]
                
        return count