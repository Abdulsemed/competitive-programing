# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.odds(root,[])
        return self.nodes
    def odds(self,root,path):
        if root == None:
            return None
        path.append(root.val)
        self.odds(root.left,path)
        self.odds(root.right,path)
        if len(path) > 2 and path[-3]%2 == 0:
                self.nodes += path[-1]
        path.pop()