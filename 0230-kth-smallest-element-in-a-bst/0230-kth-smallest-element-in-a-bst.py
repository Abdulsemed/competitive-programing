# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minim = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root)
        return self.minim[k-1]
    def traverse(self,root):
        if root == None:
            return 
        self.traverse(root.left)
        self.minim.append(root.val)
        self.traverse(root.right)