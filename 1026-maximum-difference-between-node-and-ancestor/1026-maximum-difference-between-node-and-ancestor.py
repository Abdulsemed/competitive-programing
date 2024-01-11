# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxim = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.dfs(root,root.val,root.val)
        
        return self.maxim
    def dfs(self,root,maxi,mini):
        if not root:
            return
        
        self.maxim = max(self.maxim, abs(maxi- root.val), abs(mini - root.val))
        val1, val2 =  max(root.val,maxi ), min(mini, root.val)
        self.dfs(root.left,val1,val2)
        self.dfs(root.right,val1, val2)