# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.same(root,[])
        return self.max
    def same(self,root,path):
        if root == None:
            return 0
        path.append(root.val)
        left = self.same(root.left,path)
        right = self.same(root.right,path)
        self.max = max(self.max, left+right)
        path.pop()
        if path and path[-1] == root.val:
            return max(left,right)+1
        return 0