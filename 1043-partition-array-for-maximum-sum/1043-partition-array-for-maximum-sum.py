class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dicts = {}
        def dfs(index):
            if index >= len(arr):
                return 0
            
            if (index) in dicts:
                return dicts[index]
            maxim = arr[index]
            dicts[index] = 0
            for val in range(index,min(index+k,len(arr))):
                maxim = max(maxim, arr[val])
                dicts[index] = max(dicts[index], maxim *(val-index+1) + dfs(val+1))
                
            return dicts[index]
        
        return dfs(0)