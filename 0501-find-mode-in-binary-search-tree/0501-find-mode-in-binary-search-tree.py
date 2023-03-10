# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.modes = {}
        # self.last = 0
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        arr = []
        maxim = max(self.modes.values())
        for key in self.modes:
            if self.modes[key] == maxim:
                arr.append(key)
        return arr
    def traverse(self,root):
        if not root:
            return None
        self.modes[root.val] = 1 + self.modes.get(root.val,0)
        self.traverse(root.left)
        self.traverse(root.right)