# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dicts = defaultdict(int)
    def solve(self,root,flag):
        if not root:
            return 0
        if (root,flag) in self.dicts:
            return self.dicts[(root,flag)]
        if flag:
            self.dicts[(root,flag)] = max(self.solve(root.left,False),self.solve(root.left,True)) + max(self.solve(root.right, False), self.solve(root.right, True))
        else:
            self.dicts[(root,flag)] = self.solve(root.left,True)+self.solve(root.right,True) + root.val
                                  
        return self.dicts[(root,flag)]
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.solve(root,False), self.solve(root,True))