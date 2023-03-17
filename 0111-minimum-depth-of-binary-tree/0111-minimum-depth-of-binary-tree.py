# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minim = float("inf")
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            if left == 1: return right
            elif right == 1: return left
            return min(left, right)
        return 0
    def traverse(self,root):
        if not root:
            return 1
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if left == 1: return right+1
        elif right == 1: return left+1
        return min(left,right)+1