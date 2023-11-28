class Solution:
    def __init__(self):
        self.ans = []
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        left = n
        right = n
        self.dfs(curr,left,right)
        return self.ans  
    
    def dfs(self,curr,left,right):
        if left == 0 and right == 0:
            self.ans.append(''.join(curr))
            return
        if left > 0:
            self.dfs(curr+["("],left-1,right)
        if right > 0 and left < right:
            self.dfs(curr+[")"],left,right-1)
            