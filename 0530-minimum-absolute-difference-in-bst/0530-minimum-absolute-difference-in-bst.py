# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minim = float("inf")
        self.lists = []
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("inf")
        if root.left:
            self.getMinimumDifference(root.left)
        self.lists.append(root.val)
        if len(self.lists) > 1:
            self.minim = min(self.minim, abs(self.lists[-2] - self.lists[-1])) 
        if root.right:
            self.getMinimumDifference(root.right)
        return self.minim