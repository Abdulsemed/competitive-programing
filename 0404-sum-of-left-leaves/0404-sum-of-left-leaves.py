# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        self.dfs(root,False)
        return self.sums
    def dfs(self,root,flag):
        if not root:
            return 
        if flag and not root.left and not root.right:
            self.sums += root.val
            return 
        self.dfs(root.left,True)
        self.dfs(root.right,False)