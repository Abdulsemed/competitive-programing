# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node,flag,parent):
            nonlocal root
            if not node:
                return 
            dfs(node.left,True,node)
            dfs(node.right,False,node)
            if not node.right and not node.left:
                if node.val == target:
                    if node == parent:
                        root = None
                    elif flag:
                        parent.left = None
                    else:
                        parent.right = None
                        
        dfs(root,True,root)
        return root
            