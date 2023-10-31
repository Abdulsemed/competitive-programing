# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
    def dfs(self,root):
        if not root:
            return 
        self.dfs(root.left)
        self.dfs(root.right)
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        