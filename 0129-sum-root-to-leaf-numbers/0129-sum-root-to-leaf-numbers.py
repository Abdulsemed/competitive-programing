# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumRoot = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root,"")
        return self.sumRoot
    def traverse(self,root,path):
        if not root:
            return 
        if not root.left and not root.right:
            path += str(root.val)
            self.sumRoot += int(path)
            return
        self.traverse(root.left,path+str(root.val))
        self.traverse(root.right,path+str(root.val))
        