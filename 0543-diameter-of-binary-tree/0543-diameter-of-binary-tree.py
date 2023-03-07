# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.max
        depthLeft = 0
        depthRight = 0
        if root.left:
            depthLeft = self.depth(root.left,0)
        if root.right:
            depthRight = self.depth(root.right,0)
        self.max = max(self.max,depthLeft+depthRight)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.max
    def depth(self,root,depth):
        if root == None:
            return depth
        return max(self.depth(root.left,depth+1),self.depth(root.right,depth+1))