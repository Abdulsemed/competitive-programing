# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        counter = Counter(self.path)
        if len(counter.keys()) != len(self.path):
            return False
        elif sorted(self.path) != self.path:
            return False
        return True
    def traverse(self,root):
        if root == None:
            return None
        self.traverse(root.left)
        self.path.append(root.val)
        self.traverse(root.right)