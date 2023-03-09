# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.construct(root1,root2)
        
    def construct(self,root1,root2):
        if not root1 and not root2:
            return None
        elif not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1
        left = self.construct(root1.left,root2.left)
        right = self.construct(root1.right,root2.right)
        return TreeNode(root1.val + root2.val, left,right)
        