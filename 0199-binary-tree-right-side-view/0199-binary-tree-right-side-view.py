# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rights = []
        self.size= - 1
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightTraverse(root,0)
        return self.rights
    def rightTraverse(self,root,depth):
        if root == None:
            return None
        if depth > self.size:
            self.rights.append(root.val)
            self.size += 1
        self.rightTraverse(root.right, depth+1)
        self.rightTraverse(root.left, depth+1)