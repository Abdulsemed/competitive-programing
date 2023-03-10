# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.bottomUp(root,0)[2]
    def bottomUp(self,root,count):
        if not root:
            return (0,0,count)
        left,size1,count1 = self.bottomUp(root.left,count)
        right,size2,count2 = self.bottomUp(root.right, count)
        currSum = left+right+root.val
        currSize = size1+size2+1
        count = count1 + count2
        if currSum//currSize == root.val: 
            count += 1
        return (currSum,currSize,count)