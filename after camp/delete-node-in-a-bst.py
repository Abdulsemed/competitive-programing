# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        return self.dfs(root,key)
    def dfs(self,root,key):
        if not root:
            return root
        
        if root.val > key:
            root.left = self.dfs(root.left, key)
            return root
        elif root.val < key:
            root.right = self.dfs(root.right, key)
            return root
        
        if not root.left:
            temp = root.right
            del root
            return temp
        elif not root.right:
            temp = root.left
            del root
            return temp
        else:
            succ = root
            succParent = root.right
            while succParent.left:
                succ = succParent
                succParent = succParent.left
            if root != succ:
                succ.left = succParent.right
            else:
                succ.right = succParent.right
            root.val = succParent.val
            del succParent
            return root
                