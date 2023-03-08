# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bool = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subroot(root, subRoot)
        return self.bool
    
    def subroot(self,root,sbroot):
        if self.bool or not root:
            return None 
        elif root.val == sbroot.val:
            self.bool = self.traversal(root,sbroot,True)
        self.subroot(root.left, sbroot)
        self.subroot(root.right,sbroot)
        
    def traversal(self,root1,root2,flag):
        if root1 and not root2:
            flag = False
            return flag
        elif not root1 and root2:
            flag = False
            return flag
        elif not root1 and not root2:
            return flag
        if root1.val == root2.val and flag:
            print(root1.val , root2.val)
            flag = self.traversal(root1.left, root2.left,flag)
            flag = self.traversal(root1.right, root2.right,flag)
        elif root1.val != root2.val:
            flag = False
        return flag
        