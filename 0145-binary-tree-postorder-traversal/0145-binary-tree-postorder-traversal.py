# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorder(root,[])
    def preorder(self,root,path):
        if not root:
            return path
        self.preorder(root.left,path)
        self.preorder(root.right,path)
        path.append(root.val)
        return path