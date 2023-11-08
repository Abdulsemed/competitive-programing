# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        self.height = 0
        self.dfs(0,root)
        return self.sums
    def dfs(self,height,root):
        if not root:
            return 
        if not root.left and not root.right:
            if self.height < height:
                self.sums = root.val
                self.height = height
            elif self.height == height:
                self.sums += root.val
            return
        self.dfs(height+1, root.left)
        self.dfs(height+1, root.right)
        