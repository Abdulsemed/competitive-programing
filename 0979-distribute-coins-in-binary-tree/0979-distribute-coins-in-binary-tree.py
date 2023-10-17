# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.count
    def dfs(self,root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        val = left + right + root.val
        self.count += abs(val-1)
        return val-1