# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth(root)
        if self.max >1:
            return False
        return True
    def depth(self,node):
        if node == None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.max = max(self.max,abs(right-left))
        return max(left,right)+1