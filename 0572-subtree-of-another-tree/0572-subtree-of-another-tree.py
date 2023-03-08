# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bool = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        lists = []
        anotherOne = []
        self.subroot(subRoot,anotherOne)
        self.subroot(root,lists)
        if len(anotherOne)> len(lists): return False
        if ''.join(anotherOne) in ''.join(lists):
            return True
        return False
        
    
    def subroot(self,root,lists):
        if not root:
            lists.append("#")
            return
        lists.append("@"+str(root.val))
        self.subroot(root.left,lists)
        self.subroot(root.right,lists)
            
        