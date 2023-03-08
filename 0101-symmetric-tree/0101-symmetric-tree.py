# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        node1  =root.left
        node2 = root.right
        return self.inorder(node1,node2)
        
    def inorder(self,node1,node2):
        if not node1 and node2:
            return False
        elif node1 and not node2:
            return False
        elif not(node1 and node2):
            return True
        elif node1.val != node2.val:
            return False
        l = self.inorder(node1.left,node2.right)
        r = self.inorder(node1.right, node2.left)
        return l and r