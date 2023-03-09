# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minim = 0
        self.val = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = k
        self.traverse(root)
        return self.minim
    def traverse(self,root):
        if not root:
            return
        elif self.minim:
            return
        else:
            self.traverse(root.left)
            self.val -= 1
            if not self.minim and self.val == 0:
                self.minim = root.val
                return
            self.traverse(root.right)