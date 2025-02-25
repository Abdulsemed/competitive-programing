class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = -float("inf")
        dicts = {}
        def dfs(index, flag):
            nonlocal ans
            if index >= len(arr):
                return 0
            if (index,flag) in dicts:
                return dicts[(index, flag)]
            curr = dfs(index+1, True)
            val2 = -float("inf")
            if flag:
                val1 = curr + arr[index]
                val2 = dfs(index+2, False) + arr[index]
            else:
                val1 = dfs(index+1, False) + arr[index]

            temp = max(val1,val2, arr[index])
            ans = max(ans,temp, arr[index] )
            dicts[(index,flag)] = temp
            return dicts[(index,flag)]

        dfs(0,True)
        return ans
        