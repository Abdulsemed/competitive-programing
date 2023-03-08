# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.curr = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root,[],False)
        return root
    def traverse(self,root,path,flag):
        if root == None:
            return None
        path.append(root.val)  
        self.traverse(root.right, path,False)
        self.curr += path.pop()
        root.val = self.curr
        self.traverse(root.left, path,True)