# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.bottomUp(root)
        return self.count
    def bottomUp(self,root):
        if not root:
            return (0,0)
        left,size1 = self.bottomUp(root.left)
        right,size2 = self.bottomUp(root.right)
        currSum = left+right+root.val
        currSize = size1+size2+1
        if currSum//currSize == root.val: 
            self.count += 1
        return (currSum,currSize)