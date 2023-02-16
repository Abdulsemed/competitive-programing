# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        return self.depth(root, 0)
    def depth(self,root,depth):
        if root ==None:
            return depth
        maxim = max(self.depth(root.left,depth+1), self.depth(root.right,depth+1))
        return maxim
            
        