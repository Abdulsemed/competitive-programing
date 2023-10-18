class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums= sum(nums)
        self.start = sums/k
        if sums % k:
            return False
        mask = 0
        # @cache
        def dp(currSum,count):
            nonlocal mask
            if count == k:
                return True
            if (mask,count) in memo:
                return False
            
            for val in range(len(nums)):
                if mask & (1<< val) == 0:
                    mask = mask ^ (1 << val)
                    value = currSum - nums[val]
                    if value < 0:
                        mask = mask ^ (1 << val)
                        continue
                    else:
                        add = 0
                        if value == 0:
                            add = 1
                            value = self.start
                    if dp(value,count + add): return True
                    mask = mask ^ (1 << val)
            memo[(mask, count)] = False
            return False
        memo = {}
        return dp(sums/k,0)