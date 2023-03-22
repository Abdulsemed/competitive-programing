# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            self.traverse(root,0,targetSum)
        return self.flag
    def traverse(self,root,val,target):
        if not root:
            return
        if self.flag:
            return
        val += root.val
        self.traverse(root.left,val,target)
        self.traverse(root.right,val,target)
        if val == target and not root.left and not root.right:
            self.flag = True
    