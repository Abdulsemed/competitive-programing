class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dicts = {}
        def dfs(idx,val):
            if idx >= len(text1) or val >= len(text2):
                return 0
            
            if (idx, val) in dicts:
                return dicts[(idx,val)]
            
            dicts[(idx,val)] = max(dfs(idx+1,val), (dfs(idx+1,val+1) + (text1[idx] == text2[val]) ),dfs(idx,val+1))
            return dicts[(idx,val)]
        
        return dfs(0,0)