class Solution:
    def __init__(self):
        self.maxim = - float("inf")
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dicts = {}
        def dfs(index,toogle):
            if index >= len(nums):
                return 0
            val1 = val2 = 0
            if (index,toogle) in dicts:
                return dicts[(index,toogle)]
            if toogle:
                val1 = dfs(index+1,toogle^1) -nums[index]
                val2 = dfs(index+1,toogle)
            else:
                val1 = dfs(index+1,toogle^1)+nums[index]
                val2 = dfs(index+1,toogle)
            dicts[(index,toogle)] = max(val1, val2) 
            return dicts[(index,toogle)]
        
        return dfs(0,0)