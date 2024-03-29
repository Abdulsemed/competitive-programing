# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self,root,val):
        if root == None:
            return None
        if root.val == val:
            print(root.val)
            return root
        elif root.val > val:
            return self.search(root.left,val)
        else:
            return self.search(root.right,val)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root,val)