class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dicts = {}
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
            return dicts[index]
        
        dfs(0)
        ans = 0
        glob = 0
        for key in dicts:
            if len(dicts[key]) > glob:
                glob = len(dicts[key])
                ans = key
        return dicts[ans]