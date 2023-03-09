# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.curr = float("-inf")
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)
    def traverse(self,root):
        if root == None:
            return True
        elif not (self.traverse(root.left) and self.curr < root.val):
            return False
        self.curr = root.val
        return self.traverse(root.right)