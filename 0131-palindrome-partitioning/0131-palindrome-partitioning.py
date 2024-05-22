class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        holder = []
        def dfs(index):
            if index >= len(s):
                ans.append(holder[:])
                return 
            curr = []
            for val in range(index, len(s)):
                curr.append(s[val])
                if curr == curr[::-1]:
                    holder.append("".join(curr))
                    dfs(val+1)
                    holder.pop()
                    
        dfs(0)
        return ans
                
                
                