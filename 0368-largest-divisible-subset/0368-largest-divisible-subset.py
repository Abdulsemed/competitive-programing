class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dicts = {}
        ans = 0
        glob  = 0
        nums.sort()
        def dfs(index):
            nonlocal glob, ans
            if index >= len(nums):
                return []
            
            if (index) in dicts:
                return dicts[index]
            maxim = []
            for val in range(index+1,len(nums)):
                holder = dfs(val) 
                curr = []
                if nums[val] % nums[index] == 0:
                    curr = holder
                if len(curr) > len(maxim):
                    maxim = curr.copy()
            
            dicts[index] = maxim +[nums[index]]
            if len(dicts[index]) > glob:
                glob = len(dicts[index])
                ans = index
            return dicts[index]
        
        dfs(0)
        return dicts[ans]